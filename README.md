# Zypp Electric — Bengaluru Fleet Expansion Stress Test

**An independent market-sizing and per-scooter cost case study using public sources and explicit assumptions. Not affiliated with Zypp Electric.**

## What this project asks

Zypp announced a target of **10,000 scooters in Bengaluru in May 2023**. That target is historical, not a confirmed current commitment. Later reporting said Zypp had more than 5,000 vehicles in Bengaluru in FY25 and described a broader national fleet expansion plan in 2025.

This project asks: **if management revisited a 10,000-scooter Bengaluru fleet, what would the demand and vehicle-cost assumptions need to look like?** It is an outside-in stress test, not an estimate of Zypp's internal forecast.

## What the base case says

- Estimated Bengaluru delivery demand: **1.69 million order/leg proxies per day** — 1.14M assumed quick-commerce orders plus 550K estimated food-delivery orders.
- Estimated third-party fleet market (SAM): **507,000 legs/day**, using an assumed 30% share of total demand.
- Calibrated Zypp share of third-party legs: **21.7%**, which equates to roughly 6.5% of all modeled city delivery legs. This is calibrated to a reported 6–7% Bengaluru share and is **not independent validation**.
- At 26 deliveries per active scooter-day and 85% fleet availability, the base case corresponds to about **4,978 physical scooters**.
- A 10,000-scooter scenario implies about **221,000 legs/day**, or **13.1% of modeled TAM and 43.6% of the assumed third-party fleet market**. That is a large increase in required market share, so I would not treat vehicle-level cost savings alone as sufficient evidence to expand.

The model is deliberately outside-in. City share, third-party penetration, productivity and fleet availability are assumptions or calibrations; the workbook exposes them so they can be changed.

## Vehicle-level cost comparison

The EV model uses the publicly listed Bziness XS battery-swappable scooter as a **reference vehicle**, not as a claim about Zypp's actual negotiated purchase price. The base case uses a ₹2,499/month BaaS plan with 75 kWh included, zero subsidy unless eligibility is confirmed, 100 km per active operating day and 255 active operating days/year.

Under those assumptions, modeled annual cost is approximately **₹56,576 for the EV reference** versus **₹106,275 for the petrol reference**, a difference of **₹49,700 per scooter/year (46.8%)**. This is a partial cost comparison. It excludes rider pay, financing, taxes, fleet overhead, downtime cost, residual value and actual contract terms. Higher monthly energy use than the plan allowance needs a new plan price; the model does not invent one.

## Files

| File | Purpose |
|---|---|
| `data_pack.md` | Source facts, dates, model assumptions, formula definitions and limitations |
| `excel/zypp_sizing_model.xlsx` | TAM/SAM/SOM, fleet requirement, target stress test and bear/base/bull scenarios |
| `excel/zypp_tco_model.xlsx` | Per-scooter vehicle/energy/fuel/maintenance cost comparison and utilization sensitivity |
| `recommendation_memo.md` | Decision recommendation, conditions for a pilot and data needed before scaling |
| `dashboard/index.html` | Static HTML summary of the base case; not dynamically linked to the Excel models |
| `build_sizing.py` | Regenerates the sizing workbook |
| `build_tco.py` | Regenerates the cost workbook |
| `validate_project.py` | Checks workbook integrity, sheet names, formulas and dashboard consistency |

## Rebuild the models

```bash
python3 -m pip install -r requirements.txt
python3 build_sizing.py
python3 build_tco.py
python3 validate_project.py
```

The scripts write real `.xlsx` workbooks under `excel/` and work from a fresh clone. `validate_project.py` checks the committed outputs. `dashboard/index.html` is a static snapshot; if workbook assumptions change, update the dashboard figures separately and rerun the validator.

## Recommendation in one line

**Do not approve a full 10,000-scooter deployment based on EV-versus-petrol cost alone.** First validate zone-level contracted demand, actual trips per active scooter, active fleet availability, swap-plan cost, and fully loaded per-scooter contribution. Expand in small tranches only when the operating data supports it.

## Data honesty

Public facts, analyst assumptions and calculated outputs are separated in `data_pack.md` and the workbooks. No internal Zypp data was used. The modeled savings are scenario results, not measured savings for Zypp.
