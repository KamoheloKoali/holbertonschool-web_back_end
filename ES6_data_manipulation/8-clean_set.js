export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  function findMatch(item) {
    return item.startsWith(startString);
  }

  function sliceString(item) {
    return item.slice(startString.length);
  }

  const myArray = Array.from(set);
  const myString = myArray.filter(findMatch);
  const slicedString = myString.map(sliceString);
  const ret = slicedString.join('-');

  return ret;
}
