import React, { useEffect, useState } from "react";
import Header from "../Header/Header";
import { useSelector, useDispatch } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import {getAllProductThunk, editProductThunk,
} from "../../store/productReducer";

const EditProduct = () => {
  const { productId } = useParams();

  const dispatch = useDispatch();
  const history = useHistory();

  const [title, setTitle] = useState('');
  const [price, setPrice] = useState('');
  const [description, setDescription] = useState('');
  const [category, setCategory] = useState('');
  const [brand, setBrand] = useState('');
  const [image, setImage] = useState('');
  const [count, setCount] = useState('');

  const [errors, setErrors] = useState([]);

  const product = useSelector(
      state => state.productStore.products[productId]
  );


  if(product)
{
   if(!title) {
    setTitle(product.title)
    setPrice(product.price)
    setDescription(product.description)
    setCategory(product.category)
    setBrand(product.brand)
    setImage(product.image)
    setCount(product.count)}

    const onProductEdit = async e => {
        e.preventDefault();

        await dispatch(
            editProductThunk(title, price, description, category ,brand, image, count, productId)
            );

            await dispatch(getAllProductThunk());
          };

    return (
      <div>
          <Header />
          <div className='flex flex-col mt-6 mx-10 border-b'>
        <h1 className='font-bold text-3xl'>Edit Listing</h1>
        {product && (<div className='flex flex-row items-center my-5'>
         <img src={product.image} alt='' className="w-[60px] h-[70px] mr-4"></img>
          <div className='sm:line-clamp-4'>{product.title}</div>
          </div>)}

        </div>
          <form className="mt-4 mx-10">
              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Title
                  </label>
                  <input
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      type="text"
                      size="57"
                      maxLength="50"
                      name="title"
                      onChange={e => setTitle(e.target.value)}
                      value={title}
                      required={true}
                      ></input>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Price
                  </label>
                  <input
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      type="text"
                      size="57"
                      maxLength="50"
                      name="price"
                      onChange={e => setPrice(e.target.value)}
                      value={price}
                      required={true}
                     ></input>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Description
                  </label>
                  <textarea
                      className='mb-6 border-[2px] p-2 rounded-sm' rows='4' maxLength='300'
                      name='description' onChange={e => setDescription(e.target.value)}
                      value={description}
                      ></textarea>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Category
                  </label>
                  <select
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      name="category"
                      onChange={e => setCategory(e.target.value)}
                      value={category}
                      >
                        <option value="">--Please choose a category--</option>
                        <option value="Beauty & Personal Care">Beauty & Personal Care</option>
                        <option value="Books">Books</option>
                        <option value="Clothing, Shoes & Jewelry">Clothing, Shoes & Jewelry</option>
                        <option value="Electronics">Electronics</option>
                        <option value="Groceries">Groceries</option>
                        <option value="Health & Household">Health & Household</option>
                        <option value="Pet Supplies">Pet Supplies</option>
                        <option value="Video Games">Video Games</option>
                      </select>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Brand
                  </label>
                  <input
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      type="text"
                      size="57"
                      maxLength="50"
                      name="brand"
                      onChange={e => setBrand(e.target.value)}
                      value={brand}
                      required={true}
                      ></input>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Image
                  </label>
                  <input
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      type="url"
                      size="80"
                      maxLength="50"
                      name="image"
                      onChange={e => setImage(e.target.value)}
                      value={image}
                      required={true}
                      ></input>
              </div>

              <div className="mt-3 flex flex-col border-b">
                  <label className="font-bold text-xl my-1">
                      Inventory
                  </label>
                  <input
                      className="flex self-start mb-6 p-1 text-left border-[2px] rounded-sm"
                      type="number"
                    //   size="4"
                      name="count"
                      onChange={e => setCount(e.target.value)}
                      value={count}
                      required={true}
                      ></input>
              </div>

              <div className="flex flex-row mt-5 justify-end">
                  <button
                      className="button"
                      onClick={e => {
                          history.push(`/products/${productId}`);
                      }}>
                      Cancel
                  </button>
                  <button
                      className="button ml-10"
                      onClick={e => {
                          setErrors([]);
                          onProductEdit(e);
                          history.push(`/products/${productId}`);
                      }}>
                      Submit
                  </button>
              </div>
          </form>

      </div>
  )}
  else {
    return ("Loading...")
  }
};

export default EditProduct;
