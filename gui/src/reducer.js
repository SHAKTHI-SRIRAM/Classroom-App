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
    console.log(action)
    switch (action.type) {
        case "SET_USER":
            return {
                ...state,
                user: action.user,
            }

        default:
            return {
                ...state
            }
    }
}

export default reducer;