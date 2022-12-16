import json

firstName = "James"
lastName = "Simpson"
password = "CyberStrong2023!"
email = "jamescsimpson98@gmail.com"

newUser = {
  "name": {
    "familyName": f"{lastName}",
    "givenName": f"{firstName}",
    "displayName": f"{firstName} {lastName}",
    "fullName": f"{firstName} {lastName}"
  },
  "password": f"{password}",
  "primaryEmail": f"{email}",
  "changePasswordAtNextLogin": True,
}

user_json = json.dumps(newUser)
print(user_json)


{
"primaryEmail": f"{email}",
"name": {
    "familyName": f"{lastName}",
    "givenName": f"{firstName}",
    "displayName": f"{firstName} {lastName}",
    "fullName": f"{firstName} {lastName}"
},
"suspended": false,
"password": "new user password",
"hashFunction": "SHA-1",
"changePasswordAtNextLogin": True,
"emails": [
 {
  "address": f"{email}",
  "type": "home",
  "primary": True
 }
],
"addresses": [
 {
  "type": "home",
  "customType": "",
  "streetAddress": "1600 Amphitheatre Parkway",
  "locality": "Mountain View",
  "region": "CA",
  "postalCode": "94043"
 }
],
"organizations": [
 {
  "title": "SWE",
  "primary": True,
  "type": "work",
  "description": "Software engineer"
 }
],
"phones": [
 {
  "value": "+1 nnn nnn nnnn",
  "type": "work"
 }
],
"includeInGlobalAddressList": True
}