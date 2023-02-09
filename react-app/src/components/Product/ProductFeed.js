import React from "react";
import Product from "./Product";
import ninjas from '../../Media/Banner Images/ninjas.jpg'

const ProductFeed = ({ products, user, userCart }) => {

    return (
        <div className="grid grid-flow-row-dense md:grid-cols-2 md:-mt-[450px] mx-auto lg:grid-cols-3 xl:grid-cols-4">
            {Object.entries(products).slice(0, 4).map(product => (
                <Product product={product[1]} user={user} key={product[1].id} />
            ))}
            <img className=" flex justify-self-center md:col-span-full h-[600px] w-[1400px] mt-[14px]" src={ninjas}alt="" />

            <div className="md:col-span-2">

                {Object.entries(products).slice(4, 5).map(product => (
                    <Product product={product[1]} user={user} key={product[1].id}/>
                ))}
            </div>
            {Object.entries(products).slice(5, 15).map(product => (
                    <Product product={product[1]} user={user} key={product[1].id}/>
                ))}
        </div>
    );
};

export default ProductFeed;
