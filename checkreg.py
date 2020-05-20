import requests

scc_mirror_creds = {
    'username': 'password'
}

regcode_filter = (
)

all_subs = []

for org in scc_mirror_creds:
    r = requests.get('https://scc.suse.com/connect/organizations/subscriptions',
                     auth=(org, scc_mirror_creds[org]),
                     headers={'Accept': 'application/vnd.scc.suse.com.v4+json'})
    subs = r.json()
    for sub in subs:
        sub['org'] = org
        all_subs.append(sub)

for sub in all_subs:
    if not regcode_filter or sub['regcode'] in regcode_filter:
        print(f"{sub['org']:15} {sub['regcode']:31} {sub['expires_at']:31} {sub['name']}")


