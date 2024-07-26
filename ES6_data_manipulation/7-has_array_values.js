export default function hasValuesFromArray(set, array) {
  let index = 0;

  for (const item of array) if (set.has(item)) index += 1;
  if (index === array.length) return true;
  return false;
}
