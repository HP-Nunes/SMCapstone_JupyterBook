# Key Events Timeline

<!-- https://www.sliderrevolution.com/resources/css-timeline/ -->
<br><br>

<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: Helvetica, sans-serif;
  font-weight: bold;
}
/* body {
  background: #25303B;
} */
section#timeline {
  width: 80%;
  margin: 20px auto;
  position: relative;
}
section#timeline:before {
  content: '';
  display: block;
  position: absolute;
  left: 50%;
  top: 0;
  margin: 0 0 0 -1px;
  width: 2px;
  height: 100%;
  background: #FF00BF;
}
section#timeline article {
  width: 100%;
  margin: 0 0 20px 0;
  position: relative;
}
section#timeline article:after {
  content: '';
  display: block;
  clear: both;
}
section#timeline article div.inner {
  width: 40%;
  float: left;
  margin: 5px 0 0 0;
  border-radius: 6px;
}
section#timeline article div.inner span.date {
  display: block;
  width: 60px;
  height: 50px;
  padding: 5px 0;
  position: absolute;
  top: 0;
  left: 50%;
  margin: 0 0 0 -32px;
  border-radius: 100%;
  font-size: 12px;
  font-weight: 900;
  text-transform: uppercase;
  font-weight: bold;
  background: black;
  color: #ff00bf;
  /* border: 2px solid rgba(255,255,255,0.2); */
  box-shadow: 0 0 0 4px #FF00BF;
}
section#timeline article div.inner span.date span {
  display: block;
  text-align: center;
}
section#timeline article div.inner span.date span.day {
  font-size: 10px;
}
section#timeline article div.inner span.date span.month {
  font-size: 18px;
}
section#timeline article div.inner span.date span.year {
  font-size: 20px;
  letter-spacing: 6px;
}
section#timeline article div.inner h2 {
  padding: 15px;
  margin: 0;
  color: #fff;
  font-size: 20px;
  text-transform: uppercase;
  letter-spacing: -1px;
  border-radius: 6px 6px 0 0;
  position: relative;
}
section#timeline article div.inner h2:after {
  content: '';
  position: absolute;
  top: 20px;
  right: -5px;
    width: 10px; 
    height: 10px;
  -webkit-transform: rotate(-45deg);
}
section#timeline article div.inner p {
  padding: 15px;
  margin: 0;
  font-size: 14px;
  background: #fff;
  color: #656565;
  border-radius: 0 0 6px 6px;
}
section#timeline article:nth-child(2n+2) div.inner {
  float: right;
}
section#timeline article:nth-child(2n+2) div.inner h2:after {
  left: -5px;
}
section#timeline article:nth-child(1) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(1) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(2) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(2) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(3) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(3) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(4) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(4) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(5) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(5) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(6) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(6) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(7) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(7) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(8) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(8) div.inner h2:after {
  background: #ff00bf;
}
section#timeline article:nth-child(9) div.inner h2 {
  background: #ff00bf;
}
section#timeline article:nth-child(9) div.inner h2:after {
  background: #ff00bf;
}
</style>

<section id="timeline">
  <article>
    <div class="inner">
      <span class="date">
        <span class="day">2<sup>nd</sup></span>
        <span class="month">Jul</span>
        <span class="year">2018</span>
      </span>
      <h2>Lyft acquires Motivate</h2>
      <p>By acquiring Motivate, a bikeshare operator with fleets established in New York City, Chicago, and the San Francisco Bay Area, Lyft enters the bikesharing business in a bid to rival Uber (<a href="https://www.sfchronicle.com/business/article/Lyft-acquires-Ford-GoBikes-operator-Motivate-13044094.php#photo-13693124" target="_blank">Source</a>).
      </p>
      <p>Lyft's acquistion of Motivate was closely preceded by the company successfully raising <a href="https://www.crunchbase.com/funding_round/lyft-series-i--d9ed8ce0#section-lead-investors" target="_blank">$600 million in Series I funding,</a> bumping its valuation to $15.1 billion at the time (comparatively humbling next to its closest competitor, Uber, whose valuation was estimated at $62 billion) (<a href="https://news.crunchbase.com/news/lyft-raises-600-million-in-new-funding-at-a-15-1-billion-valuation/" target="_blank">Source</a>).</p>
      <img src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_GColab/master/assets/img/stonks.png" alt="Stonks">
    </div>
  </article>
  <article>
    <div class="inner">
      <span class="date">
        <span class="day">14<sup>th</sup></span>
        <span class="month">Apr</span>
        <span class="year">2019</span>
      </span>
      <h2>E-bike woes</h2>
      <p>Shortly upon deploying its hybrid pedal-assist ebike fleet, Lyft recalled all of its 2,500 e-bikes across Washington D.C., New York City, and the San Francisco Bay Area, due to safety concerns due to braking issues (<a href="https://www.bicycling.com/news/a27287868/lyft-electric-bike-share-recall/" target="_blank">Source</a>).</p>
    </div>
  </article>
    <article>
    <div class="inner">
      <span class="date">
        <span class="day">7<sup>th</sup></span>
        <span class="month">Jun</span>
        <span class="year">2019</span>
      </span>
      <h2>Lyft sues San Francisco</h2>
      <p>Lyft filed a lawsuit against the San Francisco Municipal Transportation Agency (SFMTA) on the basis that the 10-year exclusivity contract between the company and the city precluded competitors, most notably Uber's JUMP bikes, from entering the bikesharing market. SFMTA argued that Lyft’s exclusivity agreement only covered bikeshare services with sidewalk-adjacent stations or docks, allowing competitors to offer dockless bikesharing options (<a href="https://www.sfexaminer.com/the-city/lyft-sues-san-francisco-to-block-uber-and-other-bikeshare-competitors/" target="_blank">Source</a>).</p>
    </div>
  </article>
  <article>
    <div class="inner">
      <span class="date">
        <span class="day">10<sup>th</sup></span>
        <span class="month">Jun</span>
        <span class="year">2019</span>
      </span>
      <h2>Rebranding to Bay Wheels</h2>
      <p>Lyft's public-private partnership of its bikesharing service throughout the San Francisco Bay Area is rebranded from Ford GoBikes to Bay Wheels (<a href="Lyft planned to roll back ebikes in SF (June 2019):" target="_blank">Source</a>).</p>
      <div class="center">
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">NEWS: Today, Ford GoBike has a new name — Bay Wheels. <a href="https://t.co/fmbySkW2zI">https://t.co/fmbySkW2zI</a></p>&mdash; Bay Wheels (@baywheels) <a href="https://twitter.com/baywheels/status/1138443310773678080?ref_src=twsrc%5Etfw">June 11, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
  </div>
        <p>In the meantime, Lyft planned to reintroduce its e-bike fleets in San Francisco within the month, as JUMP dockless e-bike pilot rollout came to an end (<a href="https://www.cnn.com/2019/06/11/tech/lyft-e-bikes-san-francisco/index.html" target="_blank">Source</a>).</p>
    </div>
  </article>
  <article>
    <div class="inner">
      <span class="date">
        <span class="day">31<sup>st</sup></span>
        <span class="month">Jul</span>
        <span class="year">2019</span>
      </span>
      <h2>More E-bike woes</h2>
      <p>Lyft recalls once more its e-bike fleet from San Francisco's streets following reported incidents of e-bike's batteries catching fire, less than a month after the relaunch of its e-bike fleet (<a href="https://www.theguardian.com/technology/2019/jul/31/lyft-ebike-fires-san-francisco" target="_blank">Source</a>).</p>
  <div class="center">
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Don’t think I’ll be going on a <a href="https://twitter.com/lyft?ref_src=twsrc%5Etfw">@lyft</a> <a href="https://twitter.com/baywheels?ref_src=twsrc%5Etfw">@baywheels</a> any time soon. Yikes. <a href="https://t.co/MOU9wIjgII">pic.twitter.com/MOU9wIjgII</a></p>&mdash; Zach Rutta (@zrutta44) <a href="https://twitter.com/zrutta44/status/1155147459313598465?ref_src=twsrc%5Etfw">July 27, 2019</a></blockquote> 
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
  </div>
  <p>July hadn't been all grim for Bay Wheels, as SFMTA had granted an interim permit for Lyft to deploy its dockless e-bike fleet in spite of an ongoing legal dispute between both parties. The court in the meantime had approved a preliminary injunction in Lyft's favor, preventing SFMTA from issuing permits to competing operators (<a href="https://techcrunch.com/2019/07/21/lyft-e-bikes-san-francisco/" target="_blank">Source</a>).</p>
    </div>
  </article>
  <article>
    <div class="inner">
      <span class="date">
        <span class="day">23<sup>rd</sup></span>
        <span class="month">Dec</span>
        <span class="year">2019</span>
      </span>
      <h2>Resolutions</h2>
      <p>For the third time in 2019, Lyft redeployed its e-bike fleet (although a new hybrid version capable of both dock and dockless parking), stemming from an agreed upon court settlement with SFMTA to roll out 4,000 bikes by the end of April 2020 (<a href="https://www.sfmta.com/press-releases/sfmta-and-bay-wheels-reach-agreement-4000-shared-e-bikes" target="_blank">Source</a>). The settlement also cemented Lyft's contract clause of "right of first offer" with the city to expand its bikeshare coverage and its fleet, effectively putting a stop to the ambitions of Uber's JUMP Bike (<a href="https://www.sfexaminer.com/news/supervisors-to-weigh-330000-settlement-to-lyft-over-bikeshare-dispute/" target="_blank">Source</a>).</p>
      <p></p>
    </div>
  </article>
    <article>
    <div class="inner">
      <span class="date">
        <span class="day">18<sup>th</sup></span>
        <span class="month">May</span>
        <span class="year">2020</span>
      </span>
      <h2>Game over for Uber</h2>
      <p>JUMP Bikes officially sunsets its service, days before the expiration of its bikeshare permit, and removes its entire fleet from the city's streets; leaving Bay Wheels are the sole bikeshare operator standing (<a href="https://www.sfexaminer.com/news/lyft-corners-temporary-bikeshare-monopoly-in-san-francisco/" target="_blank">Source</a>).</p>
      <blockquote class="twitter-tweet"><p lang="en" dir="ltr">‼️RT to MAKE A CHANGE‼️<br>Hey @JUMPbyUber, why is this happening? TEN semi loads of good bikes🚲trashed⁉️ Let&#39;s collaborate on a non-profit to repaint &amp; repurpose these. Give kids transportation to their first jobs👧👦<a href="https://twitter.com/Casey?ref_src=twsrc%5Etfw">@Casey</a> want to help?🙏 <a href="https://t.co/N8Uv82tr1B">pic.twitter.com/N8Uv82tr1B</a></p>&mdash; Cris Moffitt (@CrisMoffitt) <a href="https://twitter.com/CrisMoffitt/status/1263867680420966400?ref_src=twsrc%5Etfw">May 22, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    </div>
  </article>
    <article>
    <div class="inner">
      <span class="date">
        <span class="day">6<sup>th</sup></span>
        <span class="month">Jun</span>
        <span class="year">2021</span>
      </span>
      <h2>A New Generation of e-bikes</h2>
      <p>Bay Wheels unveils a new generation of e-bikes (<a href="https://www.sfweekly.com/news/lyft-introduces-new-shared-e-bikes/" target="_blank">Source</a>).</p>
      <img src="https://raw.githubusercontent.com/HP-Nunes/SMCapstone_GColab/master/assets/img/timeline1.jpg" alt="New gen Bay Wheels e-bike">
    </div>
  </article>
      <article>
    <div class="inner">
      <span class="date">
        <span class="day">23<sup>rd</sup></span>
        <span class="month">Sep</span>
        <span class="year">2021</span>
      </span>
      <h2>New rates for e-bike rides</h2>
      <p>Bay Wheels changes its overage fees for its ebike rides, as well as the per minute riding fee for e-bike rides (<a href="https://www.sfchronicle.com/sf/article/S-F-bikeshare-service-raised-its-rates-Users-16512035.php" target="_blank">Source</a>).</p>
    </div>
</section>