export default function updateStudentGradeByCity(array, city, newGrades) {
  return (
    array.filter((item) => item.location === city).map((item) => {
      const updatedItem = item;
      for (const newGrade of newGrades) {
        if (updatedItem.id === newGrade.id) {
          if ('grade' in newGrade) {
            updatedItem.grade = newGrade.grade;
          }

          updatedItem.grade = 'N/A';
        }
      }
      return updatedItem;
    })
  );
}
