This script fetche scada data related to SSP and sends email

## Prerequisites
* Install uv
* ensure config files
* ensure API access or use rnadom data
* ensure valid email smtp configuration

## Running the script
```bash
uv run main.py
```

## Config files

### secret/config.json
```json
{
    "rtDataUrlBase": "https://srv/api/values/real",
    "isRandom": true,
    "smtp": {
        "mailAddress": "user@domain.com",
        "username": "username",
        "password": "password",
        "host": "host",
        "port": 587
    },
    "receiverEmails": ["abcd@gmail.com"]
}
``` 

### secret/points.json
```json
{
    "40_G1_MW":"",
    "40_G1_MVAR":"",
    "40_G2_MW":"",
    "40_G2_MVAR":"",
    "40_G3_MW":"",
    "40_G3_MVAR":"",
    "40_G4_MW":"",
    "40_G4_MVAR":"",
    "40_G5_MW":"",
    "40_G5_MVAR":"",
    "40_G6_MW":"",
    "40_G6_MVAR":"",
    "4B1_KV":"",
    "4B2_KV":"",
    "4_ASOJ_RBPH_MW":"",
    "4_ASOJ_RBPH_MVAR":"",
    "4_DHUL4_RBPH1_MW":"",
    "4_DHUL4_RBPH1_MVAR":"",
    "4_DHUL4_RBPH2_MW":"",
    "4_DHUL4_RBPH2_MVAR":"",
    "4_KSOR_RBPH_MW":"",
    "4_KSOR_RBPH_MVAR":"",
    "4_RAJGH_RBPH1_MW":"",
    "4_RAJGH_RBPH1_MVAR":"",
    "4_RAJGH_RBPH2_MW":"",
    "4_RAJGH_RBPH2_MVAR":"",
    "ICT1_MW":"",
    "ICT1_MVAR":"",
    "ICT2_MW":"",
    "ICT2_MVAR":""
}
``` 

## References
* Using uv for python package management - https://docs.astral.sh/uv/getting-started/installation/