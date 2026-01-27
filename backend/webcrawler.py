import requests
# import json

# # Read from file and parse JSON
# with open("sample.json", "r") as f:
#     data = json.load(f)

# import json
# data = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phone": "9976770500"
# }

# json_str = json.dumps(data, indent=4)
# with open("sample.json", "w") as f:
#     f.write(json_str)


class WebCrawler:
    def __init__(self, url):
        self.url = url

    def request(self) -> str | dict:
        response = requests.get(self.url)
        
        if response.status_code == 200:
            # Check if response is JSON
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()  # Returns Python dict/list
            else:
                return response.text  # Returns string
        else:
            return "Failed"


if __name__ == "__main__":
    wb = WebCrawler("https://realpython.com/python-virtual-environments-a-primer/")
    print(wb.request())