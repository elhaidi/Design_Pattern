from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values
kpis =KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)

kpis.set_kpis(34,46,22)
kpis.set_kpis(76,29,40)
kpis.set_kpis(10,20,30)

print('\n ***** DEtaching the currentKPI observer ** \n\n')
kpis.detach(currentKPIs)
kpis.set_kpis(150,160,170)