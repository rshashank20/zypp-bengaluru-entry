# Recommendation memo — if Zypp revisits a 10,000-scooter Bengaluru fleet

**Prepared:** 12 October 2026  
**Author:** R. Shashank  
**Scope:** Outside-in scenario model; not Zypp's internal plan

## Recommendation

I would **not approve a move to 10,000 Bengaluru scooters from this model alone**. The per-scooter cost comparison favors the battery-swap EV reference under the current assumptions, but that does not prove there will be enough profitable trips to keep an expanded fleet busy.

The 10,000 Bengaluru number came from a May 2023 announcement. Later reporting said Zypp had 5,000+ vehicles in Bengaluru in FY25; in November 2025, the company discussed a larger national fleet plan. I therefore use 10,000 as a stress-test size, not as a current confirmed target.

If the question is reopened, I would test demand and unit economics in specific zones first and release additional vehicles in small tranches only when the operating data supports them.

## What the model says about demand

The base-case demand build is:

| Step | Base estimate | Basis |
|---|---:|---|
| Bengaluru quick-commerce orders/day | 1,140,000 | 9.5M national daily orders × assumed 12% city share |
| Bengaluru food-delivery orders/day | 550,000 | Midpoint of a public 500K–600K estimate |
| **TAM proxy** | **1,690,000 legs/day** | Assumes one order maps to one delivery leg |
| **SAM proxy** | **507,000 legs/day** | Assumed 30% of TAM served by third-party fleet operators |
| **Zypp base legs/day** | **~110,000** | 21.7% of SAM, calibrated to reported Bengaluru market share |
| Physical fleet corresponding to this base | **~4,978 scooters** | 26 deliveries per active scooter-day, 85% availability |

The 21.7% Zypp share is derived from the midpoint of the reported 6–7% Bengaluru market share divided by the assumed 30% third-party fleet share. That means the close fit with the reported 5,000+ Bengaluru fleet is a **calibration check, not independent validation** of the model.

At the same daily productivity and availability, 10,000 physical scooters would imply about **221,000 delivery legs/day**. That is **13.1% of the modeled total city market and 43.6% of the assumed third-party fleet market**. In practical terms, the scenario requires Zypp to more than double its modeled share of all delivery legs. The bull case lowers the required third-party share, but still requires a large capture of the serviceable market.

## What the vehicle cost comparison says

The EV reference uses the public Bziness XS battery-swap price and a ₹2,499 monthly plan with 75 kWh included. The base model assumes 100 km per active operating day, 255 active operating days/year, 3.2 kWh/100 km, petrol at ₹111/L and petrol mileage of 45 km/L. The subsidy input is zero until eligibility for the reference vehicle is confirmed.

| Annual cost item | Battery-swap EV reference | Petrol reference |
|---|---:|---:|
| Vehicle amortization | ₹14,438 | ₹23,000 |
| Insurance | ₹4,500 | ₹3,800 |
| Energy / fuel | ₹29,988 | ₹62,900 |
| Maintenance | ₹7,650 | ₹16,575 |
| **Total annual cost** | **₹56,576** | **₹106,275** |
| **Cost per km** | **₹2.22** | **₹4.17** |

That is a modeled difference of about **₹49,700 per scooter per year (46.8%)** at the base settings. The swap cost is modeled as a fixed monthly plan fee while average monthly consumption stays within the included 75 kWh. At the base setting, usage averages about 68 kWh/month. The model flags higher use rather than making up an overage rate.

This is not Zypp's full unit economics. Rider earnings, financing, tax, fleet support, downtime, swap-station overhead, vehicle residual value and contracted pricing are not included. Those costs could materially change the result.

## What I would do next

1. **Validate before committing capex.** Ask for order/trip demand by zone and time window, active vehicles by day, deliveries per active rider, contract-backed trip volumes and actual vehicle/BaaS pricing.
2. **Run an incremental pilot, not a blanket rollout.** Test an additional 500–1,000 scooters in zones with signed demand and adequate swapping access. This is a proposed test, not a company plan.
3. **Set gates using observed performance.** Track deliveries per active vehicle-day, availability, contribution per deployed vehicle after rider/fleet costs, missed service levels, swap distance/uptime and customer-contract utilization.
4. **Rerun the sizing model after the pilot.** Replace the city-share, third-party penetration, productivity and availability assumptions with zone-level observations. Do not release another tranche if the model still depends on unsupported share gains.

## Risks that could change the recommendation

- **Market-size error:** Bengaluru's 12% share of national quick-commerce demand and third-party penetration are estimates, not observed facts.
- **Different market definitions:** a company-reported market share may not use the same denominator as the delivery-leg proxy in this workbook.
- **Cost model omissions:** the cost advantage can narrow once vehicle financing, repair downtime, rider earnings, fleet support and actual swap contracts are included.
- **Target timing:** the 10,000-Bengaluru announcement dates to 2023 and should not be represented as a current company commitment.

## Decision

**Approve the data collection and a limited, contract-backed pilot; do not use this outside-in model as approval for a 10,000-scooter commitment.** The model is useful for setting the questions and showing the scale of market capture required. An actual deployment decision needs current operational and commercial data from Zypp.
