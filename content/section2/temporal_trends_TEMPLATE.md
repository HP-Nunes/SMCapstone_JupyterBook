# Temporal Analysis


## Monthly Trends

### Road Bumps

February 2020 was month with the most rides by quite a margin, with over 350,000 rides—double the 2019-2021 period average of approximately 147,422 rides per month—which can be explained by the definitive launch of Bay Wheels e-bike fleet beginning in late December 2019.  

Indeed, 2020 should have been an expected growth period for Bay Wheels: the first two months of 2020 saw an increase in ridership by over 200% compared to the same period in 2019. However that momentum was cut-short by the COVID-19 pandemic, due to the city's stay-at-home order and the general ensuing shutdown at the beginning of March 2020. While it's likely that the ridership trend seen in early 2020 would not have not carried through to the rest of the year, the COVID pandemic (and perhaps pricing changes in April 2020) certainly did put a brake on what was expected to be a formative year testing Bay Wheels' capacity to meet growing demand in San Francisco. Instead, ridership in 2020 decreased by 6% compared to 2019. 

By comparison, 2021 looks as if it is a year of slow recovery in ridership for Bay Wheels, steadily increasing throughout the months, and slowly outperforming 2019 and 2020's numbers from May 2021 onwards. 

As Bay Wheels launches a second generation of dockless e-bikes and expands its coverage of docking station throughout the city, will 2022 continue the slow and steady trend of increasing usage?

<!-- plot 1: barp_ridespermonths.html-->

<!-- plot 2: times_ridespermonths.html-->

### Riding to Riches

Bay Wheels' public historical datasets can only provide context clues to estimate the earned revenue per rides: those including the type of bikes employed (regular versus e-bikes), the duration of the trip, whether the bike was returned to a docking station or parked dockless, and whether the rider was a subscription-holder or a customer (one time purchase). By referring to the price guide and tracking changes in the fare's pricing scheme (which changed twice over the course of 2019-2021), I estimated how much a bike ride generated in revenue for Bay Wheels.

Obviously, there are a few caveats: I don't know the frequency of returning riders versus unique (one-time) riders (which would have enabled me to accurately account for the monthly/subscription fee to my total); Bay Wheels will waive riding fees under specific circumstances (for instance, docks with only e-bikes will either waive or cap how much a rider is charged); and there are many edge cases which I cannot account for (a customer disputing a charge, for instance). Thus, this is a rough yet attentive approximation to how much Bay Wheels earn in revenue <em>solely</em> from fees charged over the course of a bike ride.

Evidently, there is a pretty strong positive correlation between estimated revenue and the number of trips. 

What's more tricky to decipher is whether the price change of March 2020, which was met with some animosity by customers and subscription-holders, had an effect on the general slump in both rides and earned revenue, especially as this occured through the early period of the COVID-19 shutdown in San Francisco. What can be observed is a general recovery with a gradual increase in revenue throughout 2021, with October 2021 reaching heights not too disimilar compared to February 2020 (which saw the widespread deployment of Bay Wheels e-bike fleet). What is most striking however is that the number of rides did not significantly increase over 2021 compared to the revenue growth over that same period. As a matter of fact, although October 2021 seems to be the second most profitable month on record for Bay Wheels, it did not shatter records in bike ridership nor did it even outperform the previous month in terms of trip volumes. Perhaps this is the result of the new rates for e-bikes introduced on September 21st, 2021, which may have greatly affected Bay Wheels' bottom line. It will remain to be seen whether this trends holds for the rest of 2021.


<!-- plot 3: times_estrevpermonths.html-->

<!-- plot 4: barp_estrevpermonths.html-->

## Daily Trends

<!-- plot 5: barp_ridesperdays.html-->

## Hourly Trends

<!-- plot 6: barp_ridesperhours.html-->