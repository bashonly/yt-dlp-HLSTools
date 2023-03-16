A [yt-dlp](https://github.com/yt-dlp/yt-dlp) extractor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for handling difficult generic HLS playlists

---

Usage:

 * `--extractor-args "generic:hls_aes_uri=URI"`
   * native HLS downloader ignores the key URI from the m3u8 playlist and downloads the key from the provided `URI` instead

 * `--extractor-args "generic:hls_aes_key=KEY"`
   * native HLS downloader ignores the key URI from the m3u8 playlist and instead uses the provided `KEY` (as hex) to decrypt the fragments. This argument supersedes `hls_key_uri`

 * `--extractor-args "generic:hls_aes_iv=IV"`
   * native HLS downloader ignores the IV from the m3u8 playlist and instead uses the provided `IV` (as hex) to decrypt the fragments

 * `--extractor-args "generic:variant_query"`
   * append the query parameters from the master manifest URL to each of its media playlist URLs. Can be used in conjunction with yt-dlp's built-in `fragment_query` generic extractor argument

Multiple generic extractor args can passed using a semicolon as separator, e.g.:
```
--extractor-args "generic:hls_aes_key=0123456789abcdef;hls_aes_iv=0x9876543210fedcba;variant_query;fragment_query"
```


## Installation

Requires yt-dlp `2023.02.17` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/bashonly/yt-dlp-HLSTools/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.
