This is my solution for the assignment to create a simple API that returns the latest 6 main stories from Time.com.

The Python script runs a local server on port 7000. When you visit http://localhost:7000/getTimeStories, it fetches the homepage, finds the main article links, and returns the top 6 headlines in JSON format. It only uses built-in Python modules and does not rely on any external libraries.

OUTPUT is of this form:

[
  {
    "title": "In D.C., Start of School Meets Trump Takeover",
    "link": "https://time.com/7311513/trump-washington-dc-immigration-school-national-guard/"
  },
  {
    "title": "'I’m Afraid:' What U.S. Aid Cuts Mean for the Women of Afghanistan",
    "link": "https://time.com/7310744/afghanistan-us-aid-cuts-maternal-health/"
  },
  {
    "title": "Trump Threatens 'Complete Federal Takeover' of Washington, D.C.",
    "link": "https://time.com/7311556/trump-threatens-dc-federal-takeover-crime-figures-dispute/"
  },
  {
    "title": "The Heavy Cost of Using Weight-Loss Drugs to Get Skinny",
    "link": "https://time.com/7311517/cost-weight-loss-drugs-skinny/"
  },
  {
    "title": "1 in 30 U.S. Teens Identify as Transgender",
    "link": "https://time.com/7311082/transgender-youth-america-data-trump/"
  },
  {
    "title": "7 Ways to Soothe Your Nighttime Anxiety",
    "link": "https://time.com/7311043/how-to-treat-anxiety-at-night-racing-thoughts/"
  }
]

These are the main headlines. As the site has been upated, there was no latest-stories section as mentioned in Assignment hence , I used the main headlines and stories that were stored as static HTML and rendered first six queries.