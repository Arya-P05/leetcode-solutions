import requests
from datetime import datetime, timedelta, timezone
from collections import defaultdict

def get_call_records():
    response = requests.get('https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=5824534e18ea211f540b8210b3e1')
    return response.json()

def post_results(results):
    payload = {
        "results": results
    }
    print(payload)
    response = requests.post('https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=5824534e18ea211f540b8210b3e1', json=payload)
    return response.status_code

def get_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime('%Y-%m-%d')

def get_max_concurrent_calls(call_records):
    customer_calls = defaultdict(list)
    
    # Group calls by customer and date
    for record in call_records:
        customer_id = record['customerId']
        start_date = get_date(record['startTimestamp'])
        end_date = get_date(record['endTimestamp'] - 1)  # endTimestamp is exclusive
        
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        
        while current_date <= end_date_dt:
            date_str = current_date.strftime('%Y-%m-%d')
            customer_calls[(customer_id, date_str)].append(record)
            current_date += timedelta(days=1)
    
    results = []
    
    # Calculate max concurrent calls for each customer and date
    for (customer_id, date), calls in customer_calls.items():
        events = []
        
        for call in calls:
            events.append((call['startTimestamp'], 'start', call['callId']))
            events.append((call['endTimestamp'], 'end', call['callId']))
        
        events.sort()
        
        concurrent_calls = set()
        max_concurrent_calls = 0
        max_timestamp = None
        max_call_ids = []
        
        for timestamp, event_type, call_id in events:
            if event_type == 'start':
                concurrent_calls.add(call_id)
                if len(concurrent_calls) > max_concurrent_calls:
                    max_concurrent_calls = len(concurrent_calls)
                    max_timestamp = timestamp
                    max_call_ids = list(concurrent_calls)
            elif event_type == 'end':
                concurrent_calls.remove(call_id)
        
        results.append({
            'customerId': customer_id,
            'date': date,
            'maxConcurrentCalls': max_concurrent_calls,
            'timestamp': max_timestamp,
            'callIds': max_call_ids
        })
    
    return results

call_data = get_call_records()
call_records = call_data['callRecords']
results = get_max_concurrent_calls(call_records)
status_code = post_results(results)

print(f"POST request status code: {status_code}")
