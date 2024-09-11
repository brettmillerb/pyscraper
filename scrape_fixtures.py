import asyncio
from playwright.async_api import async_playwright

class Result:
  def __init__(self, competition, home, homescore, awayscore, away, date):
    self.competition = competition
    self.homeTeam = home
    self.homescore = homescore
    self.awayscore = awayscore
    self.awayTeam = away
    self.date = date

  def __repr__(self):
      return (f"Result(competition='{self.competition}', homeTeam='{self.homeTeam}', "
              f"homescore='{self.homescore}', awayscore='{self.awayscore}', "
              f"awayTeam='{self.awayTeam}', date='{self.date}')")

# p1 = Result("Team Valley Carpets 2nd Division", "North Sunderland", "2", "v", "3", "Hexham FC", "2024-08-03" )

async def scrape_club_info():
    async with async_playwright() as p:
        # Step 1: Launch the browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Step 2: Navigate to the webpage
        url = "https://northernfootballalliance.org.uk/clubs/view/1069"
        await page.goto(url)

        table = page.locator('.col-md-12 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1)')

        results = []
        row_index = 0

        # loop over the table rows located above and extract the information
        for row in await table.locator("tr").all():
            #  The operator ‘+=’ is a shorthand for the addition assignment operator. It adds two values and assigns the sum to a variable (left operand).
            row_index+= 1

            cell_index = 0
            cell_values = []

            # loop over the cells in the row to capture the cell information
            for cell in await row.locator("td").all():
                cell_index += 1
                cell_text = await cell.text_content()
                cell_values.append(cell_text.strip() if cell_text else "")

            if len(cell_values) >= 7:
                competition = cell_values[0]
                homeTeam = cell_values[1]
                homescore = cell_values[2]
                awayscore = cell_values[4]
                awayTeam = cell_values[5]
                date = cell_values[6]

                result_instance = Result(competition, homeTeam, homescore, awayscore, awayTeam, date)
                results.append(result_instance)

    # Print all results
    for matchResult in results:
        print(matchResult)

    # Step 5: Close the browser
    await browser.close()

# Running the scrape_club_info function
asyncio.run(scrape_club_info())
