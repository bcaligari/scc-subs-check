# scc-subs-check

Minimal Python 3.6+ script to check list the expiry date of all (or a list) of registration codes against SCC. The
mirror credentials can be found in SCC at the top right hand corner in the "proxies" tab for the specific
"organisation".

I wrote this script for personal use.

## Usage

1. Fill in `scc_mirror_creds` with a map of the mirror credentials for required accounts.
2. Optionally populate tuple `regcode_filter` with a list of registration codes to restrict reporting on.
3. Make sure it's Python 3.6+ and the `requests` module is installed.
4. `python checkreg.py`

## Checking endpoint with `curl`

```{text}
curl --silent \
    --user username:password \
    --header "Accept: application/vnd.scc.suse.com.v4+json" \
    --request GET https://scc.suse.com/connect/organizations/subscriptions | jq
```

## References:

* [SUSE Customer Centre](https://scc.suse.com/)
* [SCC API Documentation](https://scc.suse.com/connect/v4/documentation)
