import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaStar } from "react-icons/fa";
import { addToCart, removeItem } from "../../store/cartReducer";

const CartProduct = ({ product }) => {
    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartStore.addedItems);

    const addItemToCart = async () => {
        const item = {
            id: product.id,
            title: product.title,
            price: product.price,
            description: product.description,
            category: product.category,
            brand: product.brand,
            image: product.image,
        }
        await dispatch(addToCart(item))
    };

    const removeItemFromCart = () => {
        dispatch(removeItem(product));
    };

    let ratingTotal = 0;
    let ratingAvg;

    if (product && product.productReviews) {
        product.productReviews.forEach(el => {
            ratingTotal += Number(el.rating);
        });
        ratingAvg = ratingTotal / product.productReviews.length;
    }

    return (
        <div className="grid grid-cols-5">
            <a href={`/products/${product.id}`}>
                <img
                    src={product.image}
                    alt=""
                    className="h-[200px] w-[200px] object-contain"
                />
            </a>
            {/* middle section  */}
            <div className="col-span-3 mx-5">
                <p className="font-semibold text-lg">{product.title}</p>
                <div className="flex">
                    {ratingAvg ? (
                        [...Array(Math.floor(ratingAvg))].map((star, i) => (
                            <FaStar
                                size={17}
                                className="text-yellow-500"
                                key={i}
                            />
                        ))
                    ) : (
                        <FaStar size={20} color={"#e4e5e9"} />
                    )}
                </div>
                {/* Right side to add and remove buttons */}
                <p className="text-xs my-2 line-clamp-3">
                    {product.description}
                </p>
                <div className="flex flex-row justify-between items-center">
                    <div className="flex flex-row items-center">
                        <p className="mr-2">Quantity:</p>
                        <p className="font-semibold text-red-700">{product.quantity}</p>
                    </div>

                    <button
                        className="button mt-3"
                        onClick={removeItemFromCart}>
                        {" "}
                        Remove from Cart
                    </button>
                </div>
            </div>
            <div className="flex flex-col space-y-2 justify-self-end font-semibold text-lg self-start">
                <p>${product.price} </p>
            </div>
        </div>
    );
};

export default CartProduct;
