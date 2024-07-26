export default function updateStudentGradeByCity(array, city, newGrades) {
  return (
    array.filter((item) => item.location === city).map((item) => {
      const updatedItem = item;
      for (const newGrade of newGrades) {
        if (updatedItem.id === newGrade.studentId) {
          if (Object.hasOwn(newGrade, 'grade')) updatedItem.grade = newGrade.grade;
        } else updatedItem.grade = 'N/A';
      }
      return updatedItem;
    })
  );
}
