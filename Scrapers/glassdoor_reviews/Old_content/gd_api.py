import requests
import json

api_url = 'https://www.page2api.com/api/v1/scrape'
payload = {
  "api_key": "664b4d374c1a6f1e5fda2bb0ac143a21c6893e4e",
  "url": "https://nl.glassdoor.be/Reviews/Cronos-International-Reviews-E1321590.htm?filter.iso3Language=eng",
  "real_browser": True,
  "merge_loops": True,
  "premium_proxy": "us",
  "scenario": [
    {
      "loop": [
        { "wait_for": "div.gdReview" },
        { "execute": "parse" },
        { "execute_js": "document.querySelector(\".nextButton\").click()" }
      ],
      "iterations": 5,
      "stop_condition": "document.querySelector(\".nextButton\") === null"
    }
  ],
  "parse": {
    "reviews": [
      {
        "_parent": "div.gdReview",
        "opinion": "span[data-test=pros] >> text",
        "neg":" span[data-test=cons] >> text",
        "source": "glassdoor",
        "date": ".authorInfo >> text"
      }
    ]
  }
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(api_url, data=json.dumps(payload), headers=headers)
result = json.loads(response.text)

with open('gd_reviews_engCI.log', 'a') as file:
        file.write(json.dumps(result))
        file.write('\n')

print('done')