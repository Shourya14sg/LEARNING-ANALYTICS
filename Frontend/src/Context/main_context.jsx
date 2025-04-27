import { useContext } from "react";
import { createContext } from "react";

const main_context=createContext(undefined);
export function MainContextProvider({children}){
    return(
        <main_context.Provider value={{

        }}>
            {children}
        </main_context.Provider>
    )
}

export const useMainContext=()=>{
    const context = useContext(main_context);
    if(!context) throw new Error("useMainContext must be used within a MainContextProvider");
    return context;
};