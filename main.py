from scraper.domains import CompelScraper


if __name__ == "__main__":
    part_number = "ADM1485ARZ-REEL"
    compel_scraper = CompelScraper(part_number)
    df = compel_scraper.get_data()
    print(df)