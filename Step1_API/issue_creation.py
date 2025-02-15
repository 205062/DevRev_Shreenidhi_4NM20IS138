import requests


def create_work(api_url, api_key, work_data):
    headers = {"Authorization": api_key, "Content-Type": "application/json"}

    try:
        response = requests.post(api_url, headers=headers, json=work_data)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)
        return None


api_url = "https://api.devrev.ai/works.create"
api_key = "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFZTFZMSWZwY2M6ZGV2dS8xIiwiZXhwIjoxODA3MjU3NDI3LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTAwODEzMDM1OTk5MDQ0MTcwMTg3IiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMDA4MTMwMzU5OTkwNDQxNzAxODciLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFZTFZMSWZwY2MiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xWUxWTElmcGNjIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoiNG5tMjBpczEzOCIsImh0dHA6Ly9kZXZyZXYuYWkvZW1haWwiOiI0bm0yMGlzMTM4QG5tYW1pdC5pbiIsImh0dHA6Ly9kZXZyZXYuYWkvZnVsbG5hbWUiOiJTSFJFRU5JREhJIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjY0OTQyNywiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVlMVkxJZnBjYzp0b2tlbi9ZUkxjWEhCMCIsIm9yZ19pZCI6Im9yZ19JZG43WTNUY21tZ0R6U2k1Iiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFZTFZMSWZwY2M6ZGV2dS8xIn0.zQwj1XpS_oJt_R6q8i2OElOlh1Vvld0otW3FqvT0nr9FY_SxlCTxeBAq0gW6AVpXcQOo5RdChGCr4qyGvokWEmjrxh3ik1YpbzoeHp48sUukFewxhR8G1VrMCK8iselAkKSQSn1ng0ToLbCcKmRuzo49rDiA_dg0ylYB1UTb-KfmQ77v1Pl_ThcwgFN-_4d1A5K2Y3Q4bXsr0CrfDBS7Zy8jnVoz8kY0YaGZCVFndgTSP9dyrvYDgpnZthxi5yXuv_sQJZmtRf2f7l7BxzOaeOJe9mcGfWDefeP8mfTnvLCBPn3gMiPieMRVPv3R9rVJnLdqy1uRIjJyh3qCBGzcpg"

work_data = {
    "type": "issue",
    "applies_to_part": "PROD-1",
    "owned_by": ["don:identity:dvrv-us-1:devo/1YLVLIfpcc:devu/1"],
    "title": "Creation of issue",
}

result = create_work(api_url, api_key, work_data)
if result:
    print("Work created:", result)
else:
    print("Failed to create work")
