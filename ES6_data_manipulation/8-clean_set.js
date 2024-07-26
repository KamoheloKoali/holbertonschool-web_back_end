export default function cleanSet(set, startString) {
  let newWord = '';
  const toReplace = (word) => {
    const index = word.search(startString[startString.length]);
    return word.slice(0, index);
  };
  for (const word in set) {
    if (word instanceof String) {
      newWord = `${newWord}-${word.replace(toReplace(word), '')}`;
    }
  }
  return newWord;
}
