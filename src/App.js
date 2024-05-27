import React from 'react';
import Header from './components/section/Header';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Main from './components/section/Main';
import Home from './pages/Home';
import Atteck from './pages/Atteck';
import Barun from './pages/Barun';
import Cheogaji from './pages/Cheogaji';
import Chkicken from './pages/Chkicken';
import Dangchidd from './pages/Dangchidd';
import Dongki from './pages/Dongki';
import Gamach from './pages/Gamach';
import Hoolala from './pages/Hoolala';
import Kkanbu from './pages/Kkanbu';
import Kyedong from './pages/Kyedong';
import Kkubeurak from './pages/Kkubeurak';
import Mexicana from './pages/Mexicana';
import Puradak from './pages/Puradak';
import Ttobongee from './pages/Ttobongee';
import Footer from './components/section/Footer';

const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/atteck" element={<Atteck />} />
          <Route path="/barun" element={<Barun />} />
          <Route path="/cheogaji" element={<Cheogaji />} />
          <Route path="/chkicken" element={<Chkicken />} />
          <Route path="/dangchidd" element={<Dangchidd />} />
          <Route path="/dongki" element={<Dongki />} />
          <Route path="/gamach" element={<Gamach />} />
          <Route path="/hoolala" element={<Hoolala />} />
          <Route path="/kkanbu" element={<Kkanbu />} />
          <Route path="/kkubeurak" element={<Kkubeurak />} />
          <Route path="/kyedong" element={<Kyedong />} />
          <Route path="/mexicana" element={<Mexicana />} />
          <Route path="/puradak" element={<Puradak />} />
          <Route path="/ttobongee" element={<Ttobongee />} />
        </Routes>
      </Main>
      <Footer />
    </BrowserRouter>
  );
};

export default App;
