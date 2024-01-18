import requests

ENDPOINT1 = "https://catfact.ninja/#/Breeds"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT1)
    assert response.status_code == 200



def test_get_breeds():
    payload =[
  {
    "breed": "my breed",
    "country": "my_country",
    "origin": "my_origin",
    "coat": "my_coat",
    "pattern": "my_pattern"
  }
]
    response = requests.get(ENDPOINT1 + "/Breeds",json=payload)
    assert response.status_code == 200

ENDPOINT2 = "https://catfact.ninja/#/Facts/getFacts "
def test_get_facts():
    payload ={
  "fact": "cat",
  "length": 50
}

    response = requests.get(ENDPOINT2 + "/facts",json=payload)
    assert response.status_code == 200


ENDPOINT3 = "https://catfact.ninja/#/Facts/getFacts"
def test_get_facts():
    payload ={
  "fact": "aviraj",
  "length": 50
}
    
    response = requests.get(ENDPOINT3 + "/facts",json=payload)
    assert response.status_code == 200