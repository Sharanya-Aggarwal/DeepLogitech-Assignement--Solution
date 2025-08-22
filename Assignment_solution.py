#!/usr/bin/env python3

import json
import re
import urllib.request
from urllib.parse import urljoin
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.error import URLError


class MainHeadlinesHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/getTimeStories':
            try:
                stories = self.fetch_main_headlines()
                self.send_json(stories)
            except Exception as e:
                self.send_json({"error": str(e)}, status=500)
        else:
            self.send_json({"error": "Not Found. Use /getTimeStories endpoint."}, status=404)

    def fetch_main_headlines(self):
        url = 'https://time.com'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
        except URLError as e:
            raise Exception(f"Failed to fetch Time.com: {e.reason}")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

        stories = []
        seen_links = set()

        for href, title in matches:
            clean_title = re.sub(r'<[^>]+>', '', title).strip()

            if not clean_title or len(clean_title) < 10:
                continue

            full_link = urljoin(url, href)

            if re.search(r'/\d{6,7}/', full_link) and full_link not in seen_links:
                stories.append({"title": clean_title, "link": full_link})
                seen_links.add(full_link)

            if len(stories) >= 6:
                break

        if not stories:
            raise Exception("No main headlines found. Website structure may have changed.")

        return stories

    def send_json(self, data, status=200):
        payload = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(payload.encode('utf-8'))


def main():
    port = 7000
    print(f"Server running at http://localhost:{port}/getTimeStories")
    HTTPServer(('localhost', port), MainHeadlinesHandler).serve_forever()


if __name__ == '__main__':
    main()
