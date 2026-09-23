Simulation
│
├── Teams
│   ├── Players
│   └── Advisor
│
├── Companies
│
├── Scenarios
│
└── Decisions

Relationships

Team
→ assigned Company

Team
→ contains Players

Team
→ may have an Advisor

Company
→ submits Decisions

Scenario
→ affects Companies

Decision
→ generates Results
