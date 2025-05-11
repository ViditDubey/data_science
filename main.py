import requests
import json

 
def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Vidit Dubey",
        "regNo": "0827AL221144",   
        "email": "viditdubey2003@gmail.com"
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        webhook_url = data.get("webhook")
        access_token = data.get("accessToken")
        print("Webhook URL:", webhook_url)
        print("Access Token:", access_token)
        return webhook_url, access_token
    else:
        print(f"Failed to generate webhook. Status code: {response.status_code}")
        exit()


def get_sql_query():
    sql_query = """
    SELECT 
        e.name AS employee_name
    FROM 
        employees e
    JOIN 
        employees m ON e.manager_id = m.employee_id
    WHERE 
        e.salary > m.salary;
    """
    return sql_query.strip()
 
def submit_solution(webhook_url, access_token, final_query):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    submission_payload = {
        "finalQuery": final_query
    }

    response = requests.post(webhook_url, headers=headers, json=submission_payload)
    
    if response.status_code == 200:
        print("Solution submitted successfully!")
    else:
        print(f"Failed to submit solution. Status code: {response.status_code}")

 
def main():
     
    webhook_url, access_token = generate_webhook()

    
    final_sql_query = get_sql_query()

    
    submit_solution(webhook_url, access_token, final_sql_query)

if __name__ == "__main__":
    main()
