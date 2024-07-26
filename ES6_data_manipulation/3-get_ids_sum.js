import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(array) {
  return getListStudentIds(array).reduce((leftSum, rightSum) => leftSum + rightSum);
}
