# noqa: D100
import scrapy


class AnjukeBeijingSpider(scrapy.Spider):  # noqa: D101
    name = "anjuke_beijing"
    allowed_domains = ["beijing.anjuke.com"]

    def start_requests(self):  # noqa: D102
        url = "https://beijing.anjuke.com/sale/p2/"

        user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"

        cookie = "sessid=D7ABA05E-E3E9-95E3-C557-FD5F382DFDC2; aQQ_ajkguid=C432CC4B-0A7B-CC5D-2FDB-96F640D7DCCC; lps=http%3A%2F%2Fbeijing.anjuke.com%2Fsale%2F%3Fpi%3D360-cpc-bj-tyongbj2%26kwid%3D30715943244%26utm_term%3D%25e5%258c%2597%25e4%25ba%25ac%25e4%25ba%258c%25e6%2589%258b%25e6%2588%25bf%7Chttps%3A%2F%2Fcn.bing.com%2F; ctid=14; twe=2; wmda_uuid=3c5774afa3d898677ce2601a0e7abe26; wmda_new_uuid=1; wmda_session_id_6289197098934=1599053495044-9c4923b8-7617-4eb0; wmda_visited_projects=%3B6289197098934; 58tj_uuid=2f215df7-4c85-4624-9d58-7b30c3622aab; new_session=0; init_refer=https%253A%252F%252Fcn.bing.com%252F; new_uv=1; id58=c5/nK19PnrdxHnzdCWyeAg==; _ga=GA1.2.2018846987.1599053496; _gid=GA1.2.421538284.1599053496; als=0; xxzl_cid=0a278925faba4790a13c57f3c4d4f81c; xzuid=4ea249f0-75ed-4e57-8cdd-f06585d069f3"
        host = 'beijing.anjuke.com'
        yield scrapy.Request(
            url=url, headers={"User-Agent": user_agent, "Cookie": cookie}
        )

    def parse(self, response):  # noqa: D102
        pass
