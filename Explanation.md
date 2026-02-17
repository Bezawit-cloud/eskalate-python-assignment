# Explanation.md

## What was the bug?

- The code failed when setting the Authorization header if `self.oauth2_token` was an `OAuth2Token` object instead of a dict.  
- Expired dict tokens also didn’t refresh, leaving the header empty.

---

## Why did it happen?

`Client.request` assumed all tokens were dictionaries and accessed them like:

```python
self.oauth2_token['access_token']
```
- When an `OAuth2Token` object was used, this caused a TypeError.
- Expired dict tokens weren’t automatically refreshed, so headers could be missing.

## Why does your fix actually solve it?

The fix handles both token types and refreshes expired tokens:
```
if isinstance(self.oauth2_token, OAuth2Token):
    headers["Authorization"] = f"Bearer {self.oauth2_token.access_token}"
elif isinstance(self.oauth2_token, dict):
    headers["Authorization"] = f"Bearer {self.oauth2_token['access_token']}"
```
This ensures the header is always correct and all tests pass.

## One realistic edge case not covered
If a token exists but access_token is empty or None, the header becomes:
```
Authorization: Bearer None
```
This may break real API requests and isn’t tested yet.



