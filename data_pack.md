# Data pack — Zypp Electric Bengaluru fleet-sizing case

**Prepared:** 12 October 2026  
**Purpose:** Record the public facts used in the model separately from analyst assumptions.  
**Disclosure:** Independent case study; not affiliated with Zypp Electric. No Zypp internal data was used.

## First, an important date correction

The often-quoted **10,000-scooter Bengaluru target was announced on 2 May 2023**. The announcement said 2,000 scooters were already on the road and the remaining 8,000 were planned within the following two months. That deadline is historical. This project uses 10,000 as a **scenario benchmark if the company revisits that scale**, not as a current confirmed commitment.

In later public reporting, Zypp said Bengaluru's fleet exceeded 5,000 vehicles in FY25. In November 2025, Business Standard reported that Zypp had around 20,000 electric two-wheelers across its main markets and planned a national five-fold expansion over 2–3 years. The article quoted 6–7% market share in Bengaluru and 85–90% utilization. The article's definition of share and utilization may not match the simple definitions used in this workbook, so these figures are anchors for a consistency check, not interchangeable operating metrics.

## Public facts used

| ID | Fact used | Date | How it is used | Source |
|---|---|---|---|---|
| S1 | Zypp announced a Bengaluru target of 10,000 scooters; 2,000 were already deployed and 8,000 more were planned over the next two months. | 2 May 2023 | Historical scenario benchmark only; not described as a current target. | [Indian Express / PTI](https://indianexpress.com/article/business/startups/zypp-electric-e-scooters-bengaluru-next-2-months-8586983/lite/) |
| S2 | Zypp reported 5,000+ vehicles in Bengaluru in FY25 and about 6–7% market share there; it also discussed a national fleet scale-up. | 24 Nov 2025 | Context for the current scale and a rough check on the modelled baseline. | [Business Standard](https://www.business-standard.com/companies/news/zypp-electric-ipo-fleet-expansion-125112400958_1.html) |
| S3 | Quick-commerce platforms processed about 9.5 million orders per day nationally. | 17 Aug 2026 | National demand input for the city-sizing model. | [Moneycontrol](https://www.moneycontrol.com/news/technology-startup/newsletters/MCTech3/tech3-quick-commerce-firms-cross-9m-daily-orders-canva-co-founder-cameron-adams-interview-and-more/) |
| S4 | Bengaluru was estimated to have around 500,000–600,000 food-delivery orders per day. | 21 Aug 2026 | Food-delivery demand range; base input is the midpoint, 550,000/day. | [Moneycontrol](https://www.moneycontrol.com/news/business/startup/slowly-then-suddenly-rapidos-ownly-hits-50000-daily-food-delivery-orders-14012259.html) |
| S5 | Zypp reported FY25 revenue of about ₹455 crore, 100M+ cumulative deliveries and a 47% quick-commerce share of deliveries. | 28 Apr 2025 | Business context; not used to calculate Bengaluru TAM. | [Economic Times](https://economictimes.indiatimes.com/tech/startups/zypp-electric-posts-rs-455-crore-revenue-in-fy25-up-50-yoy/articleshow/120697896.cms) |
| S6 | The Bziness XS battery-swappable scooter was listed at ₹57,750 under a BaaS model; a published plan offers ₹2,499/month with 75 kWh included. | Dec 2025 / public product flyer | Reference vehicle and swap-plan inputs for the partial cost model. This is not claimed to be Zypp's actual purchase price or fleet contract. | [Autocar Professional](https://www.autocarpro.in/news/indofast-energy-and-quantum-energy-launch-affordable-electric-scooter-with-battery-swapping-130085) · [Quantum Energy plan flyer](https://quantumenergy.in/wp-content/uploads/2026/04/QE_EV_Bziness-XS_B2B-1.pdf) |
| S7 | PM E-DRIVE rules and extensions are published by the Ministry of Heavy Industries. | Updated through 2026 | The base TCO model uses **₹0 subsidy** because eligibility for the reference vehicle is not established. | [PM E-DRIVE notifications](https://pmedrive.heavyindustries.gov.in/policy_document) |
| S8 | A public industry analysis compares EV and ICE operating economics for logistics fleets. | Jun 2025 | General context only; the model's scooter inputs are stated separately rather than copied from a 3W/LCV benchmark. | [ET Infra / Praxis Global Alliance](https://infra.economictimes.indiatimes.com/news/logistics/electric-vehicles-outperform-diesel-in-indian-logistics-cost-efficiency/121773106) |

## Model assumptions — not published facts

| Assumption | Base value | Range tested | Reason / caveat |
|---|---:|---:|---|
| Bengaluru share of national quick-commerce orders | 12% | 10–15% | No directly comparable public Bengaluru share was found; this is an analyst estimate. |
| Third-party fleet share of all modeled delivery legs | 30% | 20–45% | Defines the serviceable market; not an observed market statistic. |
| Zypp share of third-party delivery legs | 21.7% | 12–28% | Calibrated from a 6.5% midpoint of the reported 6–7% Bengaluru share divided by the assumed 30% third-party fleet share. This is not independent validation. |
| Deliveries per active scooter/rider per day | 26 | 22–32 | Analyst calibration input; it is not a company-reported productivity KPI. |
| Share of physical fleet available on a typical day | 85% | 80–90% | Assumption to account for maintenance and downtime. |
| Bengaluru food delivery orders/day | 550,000 | 500,000–600,000 | Midpoint of the public estimate in S4. |
| Petrol price | ₹111/L | Change in workbook | Approximate price snapshot around October 2026, not a long-term price forecast. |
| Petrol mileage | 45 km/L | Change in workbook | Analyst assumption for an urban 110cc scooter under delivery duty. |
| EV consumption | 3.2 kWh/100 km | Change in workbook | Analyst assumption; should be replaced with a loaded-duty-cycle figure for the chosen scooter. |
| EV maintenance / petrol maintenance | ₹0.30 / ₹0.65 per km | Change in workbook | Analyst allowances, not supplier quotes. |
| Vehicle life | 4 years | Change in workbook | Analyst assumption. |

## How the sizing model works

- **Bengaluru quick-commerce demand** = national daily quick-commerce orders × assumed Bengaluru share.
- **TAM** = estimated Bengaluru quick-commerce orders + estimated Bengaluru food-delivery orders. One order is treated as one delivery leg as a simplifying proxy.
- **SAM** = TAM × assumed third-party fleet share.
- **SOM** = SAM × calibrated Zypp share of third-party legs.
- **Physical scooters required** = daily legs ÷ deliveries per active scooter-day ÷ fleet availability.
- **Target-implied legs/day** = scenario fleet size × deliveries per active scooter-day × fleet availability.

The model estimates **market demand and fleet capacity**, not revenue or profitability. It does not split the market by zone, platform contract, distance, delivery time window, multi-order batching or customer type.

## How the vehicle cost model works

The EV reference is a battery-swappable BaaS scooter priced at ₹57,750. The model uses a published ₹2,499 monthly plan that includes 75 kWh. Under the base assumption of 100 km per active operating day and 255 active operating days/year, modeled average consumption is about **68 kWh/month**, within the included limit. The model flags higher energy use rather than inventing an overage rate.

Costs included: annualized vehicle capex, insurance, BaaS subscription, energy/fuel, and per-km maintenance allowance. Costs excluded: rider earnings, financing, taxes, registration differences, tyres beyond the maintenance allowance, fleet support staff, swap-station overheads, downtime impact, insurance claims, battery/vehicle residual value and actual negotiated contracts. Treat the output as a **partial per-scooter cost comparison**, not Zypp's actual unit economics.

## Source and interpretation rules

1. A dated public statement is not automatically evidence that a plan is still active.
2. The 10,000 Bengaluru scooter target is treated as historical, while later fleet figures are described with their actual reporting dates.
3. Market estimates and model assumptions stay visibly separate.
4. The base Zypp share is calibrated from reported city share and assumed third-party penetration; a base-case “fit” is therefore a consistency check, not independent proof.
5. Replace these inputs with city-zone demand, paid trip data, active fleet availability, vehicle-level cost and contract pricing before using the model for an actual investment decision.
