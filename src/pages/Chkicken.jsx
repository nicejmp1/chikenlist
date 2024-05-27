import React, { Fragment, useEffect, useState } from 'react';
import chkickendata from '../data/chkickenPluse/chkickenPluse_2024-05-27.json';
import defaultImage from '../assets/img/defaultck.jpg';

const Atteck = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        setData(chkickendata);
    }, []);

    return (
        <div>
            <h1 className='menu__title'>
                치킨 플러스
            </h1>
            <div className='chiken'>
                {data.map((item, key) => (
                    <Fragment key={key}>
                        <ul className='menu__chiken'>
                            <div className='menu__list'>
                                <li className='menu__img'><img src={item.img || defaultImage} alt={item.Menu} /></li>
                                <li className='tit'>메뉴 : <span>{item.Menu}</span></li>
                                <li className='sub'>부가설명 : {item.Sub}</li>
                                <li className='pic'>가격 : {item.Price}</li>
                            </div>

                        </ul>

                    </Fragment>
                ))}
            </div>

        </div>
    )
}

export default Atteck
