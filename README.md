# Industrial Project Management & Control System

**Independent portfolio case study | Hassam Sajjad**

A synthetic manufacturing facility expansion with a €2 million baseline and 24-week duration. No real employer data is used.

## Deliverables
- `index.html`: standalone interactive week-12 project dashboard (open locally or deploy via GitHub Pages).
- `tasks.csv`: baseline WBS, dependencies, schedule, budget, progress and actual cost.
- `risks.csv`: risk register and mitigation actions.
- `analysis.py`: reproducible CPM and EVM calculations using Python standard library.

## Project charter
Scope: requirements, mechanical and electrical engineering, procurement, site preparation, installation, integrated testing and acceptance. Success criteria: complete all work packages within approved budget and 24 weeks; obtain signed acceptance and commissioning records. Excludes production ramp-up and ongoing maintenance. Sponsor approves scope/budget changes; project manager owns reporting; engineering leads own design release; site and quality leads own execution and acceptance.

## Baseline schedule
Finish-to-start dependencies, no lags, no resource constraints. Early start is maximum predecessor finish; early finish = start + duration. Backward pass determines late start; total float = late start − early start. Zero-float paths: A–B–D–G–I–J, A–C–D–G–I–J, A–B–D–H–I–J and A–C–D–H–I–J (24 weeks each).

## Week 12 results
| Metric | Value |
|---|---:|
| BAC | €2,000,000 |
| PV | €1,317,500 |
| EV | €1,219,500 |
| AC | €1,310,000 |
| Cost variance (EV − AC) | €-90,500 |
| Schedule variance (EV − PV) | €-98,000 |
| CPI (EV / AC) | 0.931 |
| SPI (EV / PV) | 0.926 |
| EAC (BAC / CPI) | €2,148,421 |
| VAC (BAC − EAC) | €-148,421 |

PV assumes linear budget accrual over each activity duration. EV = budget × physical completion. EAC assumes current cost efficiency persists; it is a scenario forecast, not a committed cost. SPI measures budget-weighted progress, not calendar delay.

## Management response
Equipment procurement D is 65% complete versus 75% planned and sits on critical paths. Request supplier recovery plan and weekly delivery evidence. Electrical procurement E is 90% complete versus 100% planned, with two weeks baseline float. Confirm interface readiness and do not confuse baseline float with remaining float. Review commitments and approved change orders; escalate projected overrun of about €148k to sponsor. Reforecast using remaining-duration and cost estimates before authorising acceleration. Hold weekly owner-led risk reviews. Risk scores use probability × impact (1–5 each); scores ≥15 are high priority.

## Limitations
All assumptions and results are synthetic; no resource levelling, schedule uncertainty, time-phased actuals or physical commissioning validation. Scenario edits apply to the fixed week-12 snapshot only. The project demonstrates analytical methods, not actual delivery performance.

## Run locally
Open `index.html` in a modern browser. Run `python analysis.py` in this directory to independently calculate baseline metrics.
