### Initial situation
Landlords and gas companies have few incentive to reduce gas consumption. The more you consume, the more they earn. In the city of Zurich probably still more than 50% of the houses are heated by gas.

Also you usually get a feedback of your consumption once a year, with the annual bill. But to track your consumption and also reduce it, a neartime feedback and visualisation is helpful. Gas companies usually only check the gas meter 4 times a year and will also not provide the data to you for privacy reasons.

Experiencing with weekly visualisations in the building I live, showed that 30% would easily possible if everyone would take their part.

### Goal(s)
Implement a low cost sensor which tracks the gas consumption from the gas meter. Such meters have different options for measuring consumption, from a luminicent digit to connectors to an internal bus system. Alternatively a LoRaWAN-ready add-on such as the [Cyble 5](https://www.itron.com/lam/solutions/product-catalog/cyble-5) could be used. They cost CHF ~100, but not sure what LoRaWAN they support.

<img src="/images/gasmeter.jpg" width="600" />

<img src="/images/gasmeter2.jpg" width="300" />


The sensor would send the current consumption to a server, where further analysis and visualisation can be done. As consumption heavily depends on the weather and temperature it would be wise to also track weather data from the region.

A funny and playful visualisation would help the residents from the house to save CO2 and money.

Data could also be compared between houses on a larger scale, a very interesting data set for the city, to prioritize and stear the replacement of such heating in the city. If we know the number of appartments or total living space, a map could show which houses are well isolated and which ones would eg need some adjustments, or would be replaced first to have the biggest impact.

<img src="/images/zh.png" width="600" />

Thinking further the consumption could also be estimated for the future depending on weather forecast.

### Some data
I live in an (old) house with 3 residential appartments and 2 offices. Last winter we roughly consumed 13 tons of CO2 or 4000m3 of gas! For a certain period of time 2 parties where well motivated, which showed a reduction of 35% compared to last year. Later on, only one party was palying the game seriously, which still led to a reduction of 10%.

<img src="/images/gasconsumption-q4-2022.png" width="600" />


### Some ideas
- use esp32+cam with OCR: https://github.com/jomjol/AI-on-the-edge-device (thx for the idea @Alex)
- rpi pico classification: https://github.com/code2k13/rpipico_digit_classification
- https://wiki.seeedstudio.com/Grove-Vision-AI-Module/
- https://www.housing-stat.ch/de/query/adrtoegid.html

### Resources
- [Application note](https://www.st.com/resource/en/application_note/an4636-demonstration-of-lc-sensor-for-gas-or-water-metering-based-on-stm32l073zeval-and-stm32l476rgnucleo-boards-stmicroelectronics.pdf) from STMicroelectronics on how to build a inductive sensor to measure gas consumption
- [commercial prodcut](https://www.neovac.ch/verbrauch-fairer-machen) aiming to make the consumption fair
