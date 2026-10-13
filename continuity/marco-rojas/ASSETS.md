# Marco Rojas — asset download list

Source of truth for the continuity board images. Any session can run:
"Download everything listed in continuity/marco-rojas/ASSETS.md and verify dimensions."

Paths are relative to `continuity/marco-rojas/`. Hosts that must be reachable:
`d8j0ntlcm91z4.cloudfront.net`, `d2ol7oe51mr4n9.cloudfront.net`.

| File | Expected size | Source URL |
|---|---|---|
| panels/A.png | 2752x1536 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093439_f279dc18-368a-4a2f-9b2f-9f87e0ecc0fe.png |
| panels/B.png | 2752x1536 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093236_df564e31-037f-4fd9-8eb0-81dedfa9fc5e.png |
| panels/C1.png | 2048x2048 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093237_5e57a4d8-3c54-47a7-bcbb-b1748398d7e1.png |
| panels/C2.png | 2048x2048 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093236_e71e474b-0357-4229-80ee-a1e9cb10475e.png |
| panels/D.png | 3168x1344 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093439_2984afed-0efe-41ca-a03b-4e6c85fe0cbb.png |
| panels/E.png | 2048x2048 | https://d8j0ntlcm91z4.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/hf_20261006_093236_fb4f09c9-86e8-4065-a6fd-29c16e5715b8.png |
| board.png | 2160x2700 | https://d2ol7oe51mr4n9.cloudfront.net/user_3EL6oNVV1tTsxDOFg9e7Fl9dGiZ/34eabbe3-f4ec-4a99-a00f-6e130dfcdcdc.png |

## Status

Not yet downloaded. As of 2026-10-13 the environment's network policy returns
`CONNECT tunnel failed, response 403` for the image hosts. Check that the first
URL returns HTTP 200 before downloading anything.
