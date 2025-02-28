import React from 'react'

const Header = () => {
  return (
    <div className='fixed top-0 left-0 w-full bg-gray-50 shadow-xl shadow-black/20] z-50'>
      <div className='h-[80px]  border-b-4 '></div>
      <div className='inline-block text-4xl bg-white font-extrabold ml-10 -translate-y-10'>
      <span className='pl-4'>Learning</span>
      <h1 className='ml-8'>Analytics</h1>
      </div>
    </div>
  )
}

export default Header
