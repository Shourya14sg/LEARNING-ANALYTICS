import {Route,Routes} from 'react-router-dom'
import {Header} from './Components'
import { HomePage,Analysis } from './Pages'
function App() {
  return (
    <>
    <Header/>
      <div className='mt-[100px] pt-20'>
        <Routes>
          <Route path="/" element={<HomePage/>}/>
          <Route path="/analysis"element={<Analysis/>}/>
        </Routes>
       </div>
    </>
  )
}

export default App
