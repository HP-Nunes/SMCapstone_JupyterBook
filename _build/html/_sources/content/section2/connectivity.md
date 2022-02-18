# Connectivity
<br><br>
<p style="font-size: 0.9rem;font-style: italic;"><img style="display: block;" src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/52e52df7-d399-41df-bc7e-7bbb5603fc7f/dcamvsi-0fdebd42-401b-46bd-a866-69c4216bd1b1.gif" alt="A Turning Gear"><a href="https://www.deviantart.com/retsamys/art/A-Turning-Gear-743457906">"A Turning Gear"</a><span> by <a href="https://www.deviantart.com/retsamys">RetSamys</a></span></p>

<b>Connectivity</b> performance in micro-mobility is defined by the effects of reducing the negative externalities of traffic congestion, and in creating nodal networks of mobility by inter-linking existing commuting services. In the urban commuting ecosystem, the objectives of bike-shares are <a href='https://fi.ramboll.com/-/media/files/rfi/publications/ramboll_micro-mobility-2020.pdf?la=fi' target="_blank">reducing vehicle congestion and parking demand for short and medium-distance trips</a>.

<h2>Micro-mobility: sustainable for the climate?</h2>

<p>The promise of micro-mobility services is to present an alternative to motorized transportation, contributing to the cumulative offset of emissions. However, a <a href='https://www.sciencedirect.com/science/article/pii/S1361920921004296' target="_blank"> study</a> conducted in Switzerland suggests that "personal e-scooters and e-bikes emit less CO2 than the transport modes they replace, while shared e-scooters and e-bikes emit more CO2 than the transport modes they replace". Bike-shares therefore lose in sustainability if the distance being covered substitutes less for distances covered by cars, and moreso for trips qualified as 'walking distance' (< 1 Km). Therefore, if micro-mobility bike-share is to have a substantial impact on urban emissions, it needs to fill a travelling niche equivalent to medium-driving distance.</p>

## Measuring Connectivity:

1. What is the distribution of bike-share trips by walking and driving distance?
2. How does bike-share link-up with existing public transportation nodes?
3. What is the share of bike-share trips that could be qualified as 'first' and 'last' mile commute?


## Data Overview

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 70%;
}
</style>

<br>
Over the course of three full-years of operations, San Franciscans have riden nearly 2 Km (1.24 mi) on average. Thus, the overall tendency of bike-share riding in the city is not to substitute for trips within 'walking distance' (< 1Km). Furthermore, since <a href='https://nacto.org/shared-micromobility-2019/' target="_blank">35% of all car trips in the U.S. are under 3.22 Km (2 mi)</a>, bike-share commute fills a traveling niche for trips too long for walking yet possibly costly and inneficient for driving.
<br>
We observe that the distribution of riding distance is slighly positively skewed, since the mean is greater than the median, in part due to the large number of short-distance trips.
<br><br>
<img class="center" src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_JupyterBook/master/assets/img/content/KPI_Connectivity_Distribution.png"> 
<br><br>
This beg the question: <b>what variables are affecting distance in the dataset?</b>
<br>
The most self-evident factor is the difference between <b>bike type</b>, i.e. electric bikes and non-electric bikes. If we look at distance between these categories, the difference in riding distance becomes discernable:
<br><br>
<img src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_JupyterBook/master/assets/img/content/KPI_Connectivity_1.png"> 
<br><br>
Unsurprisingly, electric bikes lead the average and median distance covered (both outpace respectively the mean and median of the entire dataset). For our purposes, we are assuming that 'docked bikes' and 'classic bikes' are both the non-electric bikes, 'classic bike' being a categorical label which was introduced at a latter stage in Bay Wheels' data collection process (without metadata to verify this claim, I'm making an informed assumptions based on my experience wrangling the raw dataset). <b>The main observation is that e-bike riders cover <b>20% more travel distance</b> on average (this is true for median distance as well) compared to the distance covered by non-ebike riders (averaging the mean distance of 'classic' and 'docked' bikes).</b>
<br><br>
If we compare distance as a factor of <b>trip type</b>, we observe that dockless rides, whether at the pick-up or drop-off points or both, tend to cover longer distances compared to the overall mean average. The reason for this is likely two-folds: 1) all dockless rides involve e-bikes (these are the only bikes that have a build-in lock), and as we know, e-bikes cover more distance on average than non e-bikes; & 2) dockless trips offer a wider coverage of areas that can be travelled in the absence of docking stations. Meaning: a trip is likely to increase in distance in areas where docking stations are either absent or present in low-density. 
<br><br>
<img align="center" src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_JupyterBook/master/assets/img/content/KPI_Connectivity_3.png"> 

## Apropos the data

Although the raw datasets provide the location of the start- and end-point of each trip, with timestamps to measure the duration of rides, it does not provide a measure of the distance covered. What I did therefore, for the main dataset of 5M+ datapoints, was to simply calculate <a href='https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance' target="_blank">Euclidean Distance</a> between each point. This serves a useful purpose to establish the <em>minimal distance</em> between two locations, however, as you all know, people can not move like birds, and get to their destination in a linear fashion.

Henceforth, a workaround solution: using <a href='https://developers.google.com/maps/documentation/distance-matrix/overview' target="_blank">Google's Distance Matrix API</a>, we can have an estimate of the <a href='https://www.igi-global.com/dictionary/network-distance/20119' target="_blank">Network Distance</a>, i.e. the shortest path distance between two points following a path, like a road. Furthermore, Google's API provides an option to estimate the optimal Network Distance for bicycle rides. Now, this also poses a normative conandrum: people don't necessarily 'optimize' their routes between A and B, and even if they do, traffic and the entropy of sharing the road does not always yield an optimal trip by distance and time. But it's the best option that we have with our current limitations, and offers much better real-world accuracy compared to Euclidean Distance.

However, a snaffu is that Google's Distance Matrix API is a paid service (which can be offset thanks to <a href='https://cloud.google.com/free' target="_blank">Google Cloud's free trial offer</a>; yet, even with $300 worth of credit, running the API through 5M+ datapoints will do me no good. Statistics is the art of frugality, therefore I had to be selective in choosing the sample of trips I wanted distance estimates for.

Another hiccup is the limitation of the spatial resolution innate in the dataset. Now, datapoints starting and ending at docked stations have a high degree of spatial resolution, however, dockless trips, understandably out of the ethical necessity to maintain the privacy of its users, yield a much lower spatial resolution (up to only two or three decimal places on each start- and end-point's geographic coordinates). Additionally, these points are laid-out in a grid-like fashion, to further anonymise the directionality and density of those trips. But this level of accuracy is good enough to aggregate these trips by neighborhoods and census tracts. However, running Google's API on dockless trips will yield a less accurate estimate of distance compared to docked trips.

And I'm afraid we're not quite done yet: you see, some trips start and end at the <em>same location</em>! These are what I call 'looped' trips. For dockless trips, this is possibly a post-processing artifact from rounding-up coordinates. For docked trips however, and I was quite surprised to observe this in the dataset, 'looped' trips, which start and end at the same pick-up/drop-off station, are quite popular! The good news is that I can make certain inferences about ridership behavior by location and time (for example, 'looped trips' in touristy areas might serve as a choice alternative to rental bikes). The bad news is...we can't estimate accurately for a distance...What I can do if I so choose instead is to interpolate by taking the average of meter distance covered by seconds, for example, and apply it to the time elapsed for those trips. But that's beside what we're trying to accomplish for this particular KPI.

As you understand, we are required to be strategic about getting the most out of the dataset, and be deliberate on how to select representative samples over different data dimensionalities. 
<!-- ## 1. A bike! a bike! my city for a bike! -->


