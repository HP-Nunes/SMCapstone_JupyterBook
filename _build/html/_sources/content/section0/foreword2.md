# Foreword 2 (test)

## The Rise of Micromobility

Like old-wine in new bottles, bicycle-sharing systems are nothing inherently new ([Copenhagen City Bikes](https://en.wikipedia.org/wiki/Copenhagen_City_Bikes) launched in 1995), but the world we find ourselves in is much different than what it was even just 20 years ago. Specifically, we live in a world with ever-increasing population-densifying cities; [by 2050](https://www.unfpa.org/urbanization), most of humanity will be urban-dwellers. Consequently, the demands and expectations for what public transportation systems can handle are changing rapidly, for many different reasons. One can mention the unbearability of air pollution caused by congested traffic arteries, the political pressure for decision-makers to curb greenhouse gas emissions, the changing philosophies of urban planners towards liveable and walkable cities, and the prohibitive costs of car ownership, to name just a few. As such, a great deal of transportation pressure in urban spaces isn't to primarily cover large distances, but in enabling pathways of [micromobility](https://en.wikipedia.org/wiki/Micromobility) to fill transportation gaps without massively transforming existing infrastructure, while attaining standards of environmental sustainability, and providing an affordable mode of transportation for both commuters and operators.

> Micromobility is defined as mode of transportation which are fully or partially human-powered vehicles such as bikes or scooters operating at speeds under 25 km/h (15 mph). 

Bikesharing, the shared use of bikes for individuals at publically available access points, is one prominent example of micromobility, and a rapidly growing industry accounting for 84 million trips in 2018, twice the number of trips compared to the previous year<sup>[1](#myfootnote1)</sup>. Its market-size was valued at USD 3.1 billion in 2018, with a forecasted compound annual growth rate of 17% as of 2020<sup>[2](#myfootnote2)</sup>.

In the United States, bikesharing is predominant in large, densely populated cities such as New York City, which accounted for 40% of all bike trips in the country for 2017 alone<sup>[3](#myfootnote3)</sup>. Six cities accounted for 84% of all station-based (meaning that the bikes had to be returned to a docking station) bikesharing trips in 2018:

<img align="center" width="800" height="600" src="https://nacto.org/wp-content/uploads/2019/04/Station-Based-Bike-Share-Ridership.png"> 

[source](https://nacto.org/shared-micromobility-2018/)

According to an INRIX Research study, micromobile commuting options such as bikes and scooters could replace nearly 50% of short-distance (< 3 miles) vehicle trips in the U.S.<sup>[4](#myfootnote4)</sup>. San Francisco, the focus of this project's analysis, ranked 10th<sup>[5](#myfootnote5)</sup> in INRIX's ranking of U.S. cities with the greatest micromobility potential, an index based on facors including efficient and cost-effective travel, reduced traffic congestion, decreased emissions impact, and anticipated effects on the local economy. 

For a comprehensive overview of the main players in the micromobility industry, consult the diagram below by <a href='https://micromobility.io/landscape' target='_blank'>Micromobility Industries</a> (hover over the image for a zoomed-in view to the right).
<br>

<!-- Adding a Zoom function
https://www.w3schools.com/howto/howto_js_image_zoom.asp -->
<style>
* {box-sizing: border-box;}

.img-zoom-container {
  position: relative;
}

.img-zoom-lens {
  position: absolute;
  border: 1px solid #d4d4d4;
  /*set the size of the lens:*/
  width: 40px;
  height: 40px;
}

.img-zoom-result {
  border: 1px solid #d4d4d4;
  /*set the size of the result div:*/
  width: 300px;
  height: 300px;
}
.inline-block-child {
  display: inline-block;
}
</style>
<script>
function imageZoom(imgID, resultID) {
  var img, lens, result, cx, cy;
  img = document.getElementById(imgID);
  result = document.getElementById(resultID);
  /* Create lens: */
  lens = document.createElement("DIV");
  lens.setAttribute("class", "img-zoom-lens");
  /* Insert lens: */
  img.parentElement.insertBefore(lens, img);
  /* Calculate the ratio between result DIV and lens: */
  cx = result.offsetWidth / lens.offsetWidth;
  cy = result.offsetHeight / lens.offsetHeight;
  /* Set background properties for the result DIV */
  result.style.backgroundImage = "url('" + img.src + "')";
  result.style.backgroundSize = (img.width * cx) + "px " + (img.height * cy) + "px";
  /* Execute a function when someone moves the cursor over the image, or the lens: */
  lens.addEventListener("mousemove", moveLens);
  img.addEventListener("mousemove", moveLens);
  /* And also for touch screens: */
  lens.addEventListener("touchmove", moveLens);
  img.addEventListener("touchmove", moveLens);
  function moveLens(e) {
    var pos, x, y;
    /* Prevent any other actions that may occur when moving over the image */
    e.preventDefault();
    /* Get the cursor's x and y positions: */
    pos = getCursorPos(e);
    /* Calculate the position of the lens: */
    x = pos.x - (lens.offsetWidth / 2);
    y = pos.y - (lens.offsetHeight / 2);
    /* Prevent the lens from being positioned outside the image: */
    if (x > img.width - lens.offsetWidth) {x = img.width - lens.offsetWidth;}
    if (x < 0) {x = 0;}
    if (y > img.height - lens.offsetHeight) {y = img.height - lens.offsetHeight;}
    if (y < 0) {y = 0;}
    /* Set the position of the lens: */
    lens.style.left = x + "px";
    lens.style.top = y + "px";
    /* Display what the lens "sees": */
    result.style.backgroundPosition = "-" + (x * cx) + "px -" + (y * cy) + "px";
  }
  function getCursorPos(e) {
    var a, x = 0, y = 0;
    e = e || window.event;
    /* Get the x and y positions of the image: */
    a = img.getBoundingClientRect();
    /* Calculate the cursor's x and y coordinates, relative to the image: */
    x = e.pageX - a.left;
    y = e.pageY - a.top;
    /* Consider any page scrolling: */
    x = x - window.pageXOffset;
    y = y - window.pageYOffset;
    return {x : x, y : y};
  }
}
</script>

<div class="img-zoom-container">
    <div class='parent'>
        <div class='child inline-block-child'>
  <img id="myimage" src="https://github.com/HP-Nunes/SMCapstone_JupyterBook/blob/master/assets/img/content/Micromobility_Landscape.png?raw=true" width="800" height="600" alt="Micromobility Landscape: https://micromobility.io/landscape">
        </div>
        <div class='child inline-block-child'>
  <div id="myresult" class="img-zoom-result"></div>
        </div>
    </div>
</div>

<script>
imageZoom("myimage", "myresult");
</script>

## Bikesharing: A Tenuous Affair

Bikesharing systems tend to be public-private partnerships, with ridesharing companies like Lyft and Uber involved in the micromobility market, seeking to set the tone for the industry. Uber's strategy, for instance, is to build and own the urban transportation's ecosystem within its app delivery service, providing an array of ridesharing transportation options including electric scooters and bikes<sup>[6](#myfootnote6)</sup>. However these partnerships are politically liable to controversy and pushback, as they are signifiers of the prevailing trend of the privatization of public commons and services.

<!-- <img align="left" width="400" height="500" src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_JupyterBook/master/assets/img/content/lyft2.jpg" style="margin-right:25px">  -->
In San Francisco, Lyft's Bay Wheels has seen backlash caused by unpopular rental pricing changes in 2020 and 2021. Horace Dediu, a leading analyst credited with coining the term "micromobility", stated: *“I see bikeshare systems as public transit that should be funded and looked upon as public transit, not as a standalone function that has to be in the black all the time to operate.”*<sup>[7](#myfootnote7)</sup>.

Although the market of micromobility is still maturing, it remains to be seen how the industry will evolve with the disturbances of daily-life brought upon by the COVID-19 pandemic.

## The Paradigm Shift of Dockless E-Bikes 

<img align="left" style="margin-right:25px" width="400" height="300" src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_JupyterBook/master/assets/img/content/lyft3.jpg">

The formative model of bike-sharing was docked: rent a docked-bike at a pick-station, and drop-it off at the nearest drop-off station to your destination. Dockless bikes remove this barrier, since these bikes are not bounded to a station. This has the advantage of widening the scope of mobility for commuters, requiring just the app to geolocate and borrow the nearest bike. However this poses challenges for operators (in terms of durability, maintenance etc.) and cities, such as added clutter on sidewalks (an issue similar to the highly publicized roll-out of e-scooters, for instance).

Dockless bikes are designed for short, spontaneous trips, such as a commuter first-or-last mile option. They also present a much cheaper alternative to a potential bus trip or traditional bike share daily pricing scheme.

<!-- ![](./img/dockless.jpg "title-2") -->

<!-- [source](https://techcrunch.com/2019/07/21/lyft-e-bikes-san-francisco/) -->

<!-- [source](https://twitter.com/baywheels/status/1199031957822291973) -->

<!-- https://blog.altaplanning.com/the-dockless-bike-share-revolution-eb62698d81f8 -->
<br><br><br>
<p>
<b>Learn more:</b>

<a name="myfootnote1">1</a>: <a href='https://nacto.org/program/bike-share-initiative/' target="_blank"> National Association of City Transportation Officials</a>
<br>
<a name="myfootnote2">2</a>: <a href='https://www.globenewswire.com/news-release/2020/02/10/1982550/0/en/Global-Micro-Mobility-Market-was-valued-at-USD-3-1-billion-Observing-a-CAGR-of-17-0-during-2019-2024-VynZ-Research.html#:~:text=Filings%20Media%20Partners-,Global%20Micro%2DMobility%20Market%20was%20valued%20at%20USD%203.1%20billion,during%202019%E2%80%932024%3A%20VynZ%20Research&text=NEW%20YORK%2C%20Feb.,USD%203.1%20billion%20in%202018' target="_blank">VynZ Research</a>
<br>
<a name="myfootnote3">3</a>: <a href='https://www.wired.com/story/americans-falling-in-love-bike-share/' target="_blank">WIRED: Americans Are Falling in Love With Bike Share</a>
<br>
<a name="myfootnote4">4</a>: <a href='https://inrix.kinsta.cloud/blog/managing-micromobilty-to-success/' target="_blank">INRIX Research: Managing Micromobilty to Success
</a>
<br>
<a name="myfootnote5">5</a>: <a href='https://inrix.com/press-releases/micromobility-study-us-2019/' target="_blank">INRIX Research: Shared Bikes and Scooters Could Replace Nearly 50 Percent of Downtown Vehicle Trips</a>
<br>
<a name="myfootnote6">6</a>: <a href='https://www.wired.com/story/uber-bid-dominance-mobility/?mbid=BottomRelatedStories' target="_blank">WIRED: Uber's New Bid for Dominance: Controlling Every Way You Move</a>
<br> 
<a name="myfootnote7">7</a>: <a href='https://www.bloomberg.com/news/articles/2021-06-02/lyft-launches-an-e-bike-for-the-post-covid-commute' target="_blank">CITYLAB: Lyft’s New E-Bike Aims to Conquer the Post-Pandemic City</a>
<br> 
</p>


