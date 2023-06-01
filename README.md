### Initial situation
Landlords and gas companies have few incentive to reduce gas consumption. The more you consume, the more they earn. In the city of Zurich probably still more than 50% of the houses are heated by gas.

Also you usually get a feedback of your consumption once a year, with the annual bill. But to track your consumption and also reduce it, a neartime feedback and visualisation is helpful. Gas companies usually only check the gas meter 4 times a year and will also not provide the data to you for privacy reasons.

Experiencing with weekly visualisations in the building I live, showed that 30% would easily possible if everyone would take their part.

### Goal(s)
Implement a low cost sensor which track the gas consumption on the gas meter. Such meters have different options for measuring consumption, from a luminicent digit to connectors to a internal bus. Alternatively a LoRaWAN-ready add-on such as the [Cyble 5](https://www.itron.com/lam/solutions/product-catalog/cyble-5) could be used. They cost CHF ~100, but not sure what LoRaWAN they support.
<img src="/images/gasmeter.jpg" width="600" />


The sensor could send the current consumption to a server. As consumption heavily depends on the weather and temperature it would be wise to also track weather data from the region.

A funny and playful visualisation would help the residents to save CO2 and money. Data could also be compared between houses, a very interesting data set for the city, to prioritize and stear the replacement of such heating in the city. If we know the number of appartments or total living space, a map could show which houses are well isolated and which ones would need some adjustments.

Thinking further the consumption could also be estimated for the future depending on weather forecast.

### Some data
I live in an (old) house with 3 residential appartments and 2 offices. Last winter we roughly consumed 13 tons of CO2 or 4000m3 of gas! For a certain period of time 2 parties where well motivated, which showed a reduction of 35% compared to last year. Later on, only one party was palying the game seriously, which still led to a reduction of 10%.
<img src="/images/gasconsumption-q4-2022.png" width="600" />
