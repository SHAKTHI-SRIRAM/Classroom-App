export const initialState = {
    user: null,
    is_teacher: false,
    is_student: false,
    classrooms: [],
    tests: [],
    homeworks: [],
    chats: [],
}

const reducer = (state, action) => {
    switch (action.type) {
        case "SET_USER":
            return {
                ...state,
                user: action.user,
            }

        case "SET_CLASSROOMS":
            return {
                ...state,
                classrooms: action.classrooms,
            }

        case "SET_TESTS":
            return {
                ...state,
                tests: action.tests,
            }

        case "SET_HOMEWORKS":
            return {
                ...state,
                homeworks: action.homeworks,
            }
            
        case "SET_CHATS":
            return {
                ...state,
                chats: action.chats,
            }

        case "SET_TEACHER":
            return {
                ...state,
                is_teacher: action.teacher,
            }

        case "SET_STUDENT":
            return {
                ...state,
                is_student: action.student,
            }
            
        default:
            return {
                ...state
            }
    }
}

export default reducer;