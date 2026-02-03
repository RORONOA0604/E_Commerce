import { createSlice } from "@reduxjs/toolkit";
import { store } from "../store";

export const UserSlice = createSlice({
    name:'UserSlice',
    initialState: {
        user:null
    },
    reducers: {
          setUser(state,action){
            state.user = action.payload
          }
    }
})
export const{setUser} =UserSlice.actions

export const UserSlicePath = (store) => store.UserSlice.user