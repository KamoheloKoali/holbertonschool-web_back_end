export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, it was the seventh-highest income county in the United States
    with a per capita personal income of ${budget.income}. As of 2015, San Fransisco
    proper had a GPD of ${budget.gpd} and GPD per capita of ${budget.capita}.`;
}
