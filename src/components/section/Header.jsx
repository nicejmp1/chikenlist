import React from 'react'

import { headerMenus } from "../../data/header"
import { Link } from 'react-router-dom'

const Header = () => {
    return (
        <header id='header' role='banner'>
            <h1 className='header__logo'>
                {/* Link 컴포넌트 사용 */}
                <Link to="/">
                    <em></em>
                    <span>치킨브랜드 모음집</span>
                </Link>
            </h1>
            <nav className='header__menu'>
                <ul className='menu'>
                    {headerMenus.map((menu, key) => (
                        <li key={key}>
                            <Link to={menu.src}>
                                {menu.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </header>
    )
}

export default Header
