import React, { Fragment, useEffect, useState } from 'react';
import Atteckdata from '../data/atteckChicken/atteckChicken_2024-05-27.json';

const Atteck = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        setData(Atteckdata);
    }, []);

    return (
        <div>
            <h1 className='menu__title'>
                <span>순살만공격 치킨</span>
            </h1>
            <div className='chiken'>
                {data.map((item, key) => (
                    <Fragment key={key}>
                        <ul className='menu__chiken'>
                            <li className='menu__img'><img src={item.img} alt={item.Menu} /></li>
                            <div className='menu__list'>
                                <li className='tit'>메뉴 : <span>{item.Menu}</span></li>
                                <li className='sub'>부가설명 : {item.Sub}</li>
                                <li className='pic'>가격 : <span>{item.Price}</span></li>
                            </div>
                        </ul>
                    </Fragment>
                ))}
            </div>
        </div>
    )
}

export default Atteck
