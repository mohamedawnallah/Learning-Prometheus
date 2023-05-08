## Promothesus Architecture
![Promothesus Architecture](assets/architecture.png)

## What to Instrument

Prometheus instrumentation documentation says:
```
The short answer is to instrument everything. Every library, subsystem and service should have at least a few metrics to give you a rough idea of how it is performing.
```
Instrument:
- Services
- Libraries

## Service Instrumentation
- Online-Serving System:
1. An online-serving system is one where a human or another system is expecting an immediate response. For example, most database and HTTP requests fall into this category.
2. The key metrics in such a system are `the number of performed queries`, `errors`, and `latency`. `The number of in-progress requests` can also be useful.
3. Should mentored on both the client and server side 
- Offline-Serving System
1. For offline processing, no one is actively waiting for a response, and batching of work is common. There may also be multiple stages of processing.
2. For each stage, track the items coming in, `how many are in progress`, `the last time you processed something`, and `how many items were sent out`. If batching, you should also `track batches going in and out`.
3. If batching, then track the metrics for batches and individual items
4. They're running continously kind of streaming
- Batch Jobs
1. Unlike Offline-Serving Systems, Batch jobs run on regular times
2. Push Gateway used to scrape batch jobs
3. The key metric of a batch job is `the last time it succeeded`. It is also useful to track `how long each major stage of the job took`, `the overall runtime` and `the last time the job completed (successful or failed)`

## Library Instrumentation
- A Library should provide instrumentation with no additional configuration required by users 
- Depending on how heavy the library is, track ```internal errors``` and ```latency within the library itself```, and any general statistics you think may be useful.

## How much to instrument
It's subjective more than objective. There is no hard rule to follow as there is allow a tradeoff between the benefits you get from the instrumentation and the operational cost.

## Reload Promotheus Configurations on the Flay
- Post Request to Promothesus Reload API Endpoint
- SigHub Signal to the Promothesus Process

## Types of Rules
- Recording Rules:
1. Naming Conventions -> ```level:metric:operations```
2. Avoid using rules for long range vectors, as such queries tend to be expensive, and running them regularly can cause performance problems
- Alerts
