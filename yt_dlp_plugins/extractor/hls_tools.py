from yt_dlp.update import version_tuple
from yt_dlp.version import __version__

if not ((2023, 2, 17) <= version_tuple(__version__) < (2023, 3, 21, 231235)):
    raise ImportError('Only yt-dlp versions between 2023.02.17 and 2023.03.21.225804 can use this plugin')

from yt_dlp.utils import parse_qs, traverse_obj, update_url_query
from yt_dlp.extractor.generic import GenericIE


class Generic_HLSToolsIE(GenericIE, plugin_name='HLSTools'):
    def _real_extract(self, url):
        ret = super()._real_extract(url)

        hls_aes = traverse_obj(self._downloader.params, ('extractor_args', 'generic', {
            'uri': ('hls_aes_uri', 0, {lambda x: x or None}),
            'key': ('hls_aes_key', 0, {lambda x: x or None}),
            'iv': ('hls_aes_iv', 0, {lambda x: x or None}),
        }))

        for fmt in traverse_obj(ret, ((None, ('entries', ...)), 'formats', ..., {dict})):
            if hls_aes:
                fmt['hls_aes'] = hls_aes
            if self._configuration_arg('variant_query'):
                query = traverse_obj(fmt, ('manifest_url', {parse_qs}))
                if query:
                    fmt['url'] = update_url_query(fmt['url'], query)

        return ret


__all__ = []
