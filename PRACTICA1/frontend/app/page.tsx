'use client'
import HocWithoutSesion from 'hoc/hocWithoutSesion';
import HomeView from 'views/home';

const HomePage =() =>{
  return (
    <HomeView/>
  );
}

export default HocWithoutSesion(HomePage);
